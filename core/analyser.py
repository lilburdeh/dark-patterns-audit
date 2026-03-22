"""Orchestrates the dark patterns analysis pipeline."""

from __future__ import annotations

import json
import re
from datetime import datetime, timezone

import anthropic

from config.settings import MODEL, TEMPERATURE, MAX_TOKENS, get_api_key
from core.prompt_builder import load_ontology, build_system_prompt, build_user_message


def _parse_json_response(text: str) -> dict:
    """Extract and parse JSON from the model response.

    Handles both raw JSON and JSON wrapped in markdown code fences.
    """
    # Try direct parse first
    text = text.strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass

    # Try extracting from markdown code fence
    match = re.search(r"```(?:json)?\s*\n?(.*?)\n?```", text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group(1).strip())
        except json.JSONDecodeError:
            pass

    raise ValueError(
        "Could not parse JSON from model response. "
        f"Response starts with: {text[:200]}..."
    )


def _validate_result(result: dict) -> dict:
    """Validate that the result has the expected structure."""
    required_keys = ["audit_metadata", "summary", "findings", "strategies_checked"]
    for key in required_keys:
        if key not in result:
            raise ValueError(f"Missing required key in response: {key}")

    # Ensure summary counts match findings
    findings = result["findings"]
    summary = result["summary"]
    summary["total_findings"] = len(findings)
    summary["high"] = sum(1 for f in findings if f.get("severity") == "High")
    summary["medium"] = sum(1 for f in findings if f.get("severity") == "Medium")
    summary["low"] = sum(1 for f in findings if f.get("severity") == "Low")

    # Recalculate risk level
    if summary["high"] > 0:
        summary["risk_level"] = "High"
    elif summary["medium"] > 0:
        summary["risk_level"] = "Medium"
    elif summary["low"] > 0:
        summary["risk_level"] = "Low"
    else:
        summary["risk_level"] = "Clean"

    # Update strategies_checked counts
    for strategy_name, info in result.get("strategies_checked", {}).items():
        info["findings_count"] = sum(
            1 for f in findings if f.get("strategy") == strategy_name
        )

    return result


def run_audit(
    image_bytes: bytes,
    source_type: str,
    source_description: str,
    html_source: str | None = None,
) -> dict:
    """Run a full dark patterns audit on a screenshot.

    Args:
        image_bytes: The screenshot image as bytes.
        source_type: Either "screenshot" or "url".
        source_description: Description of the source (filename or URL).

    Returns:
        Structured audit result dict.

    Raises:
        ValueError: If API key is missing or response cannot be parsed.
        anthropic.APIError: If the API call fails.
    """
    api_key = get_api_key()
    if not api_key:
        raise ValueError(
            "No Anthropic API key found. Set ANTHROPIC_API_KEY in your "
            "environment or Streamlit secrets."
        )

    # Load ontology and build prompt
    ontology = load_ontology()
    system_prompt = build_system_prompt(ontology)
    user_content = build_user_message(image_bytes, source_description, html_source)

    # Call Claude API
    client = anthropic.Anthropic(api_key=api_key)
    response = client.messages.create(
        model=MODEL,
        max_tokens=MAX_TOKENS,
        temperature=TEMPERATURE,
        system=system_prompt,
        messages=[{"role": "user", "content": user_content}],
    )

    # Extract text from response
    response_text = response.content[0].text

    # Parse and validate
    result = _parse_json_response(response_text)
    result = _validate_result(result)

    # Ensure metadata is populated
    metadata = result.setdefault("audit_metadata", {})
    metadata.setdefault("audit_timestamp", datetime.now(timezone.utc).isoformat())
    metadata.setdefault("ontology_version", ontology.get("version", "1.0"))
    metadata["model"] = MODEL
    if source_type == "url" and source_description:
        metadata.setdefault("url", source_description)

    return result
