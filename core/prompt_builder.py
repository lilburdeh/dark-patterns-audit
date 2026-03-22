"""Constructs analysis prompts from the ontology and user input."""

from __future__ import annotations

import base64
import json
from pathlib import Path

from config.settings import ONTOLOGY_PATH, ONTOLOGY_VERSION


def load_ontology() -> dict:
    """Load the ontology JSON file."""
    with open(ONTOLOGY_PATH) as f:
        return json.load(f)


def _format_ontology_for_prompt(ontology: dict) -> str:
    """Format the full ontology as structured text for the system prompt."""
    lines = []
    for strategy in ontology["strategies"]:
        lines.append(f"\n## {strategy['name']} (High-Level Strategy)")
        lines.append(f"Definition: {strategy['definition']}")

        # Include regulatory references if present
        reg_refs = strategy.get("regulatory_refs", [])
        if reg_refs:
            ref_strs = []
            for ref in reg_refs:
                fw = ref.get("framework", "")
                cat = ref.get("category", "")
                cats = ref.get("categories", [])
                if cats:
                    ref_strs.append(f"{fw}: {', '.join(cats)}")
                elif cat:
                    ref_strs.append(f"{fw}: {cat}")
            lines.append(f"Regulatory relevance: {'; '.join(ref_strs)}")

        for angle in strategy["angles"]:
            lines.append(f"\n### {angle['id']}: {angle['name']} (Meso-Level)")
            lines.append(f"Definition: {angle['definition']}")
            lines.append(f"What to look for: {angle['what_to_look_for']}")

            # Include detection examples if present
            examples = angle.get("detection_examples", [])
            if examples:
                lines.append(f"Detection examples: {'; '.join(examples)}")

            if angle["patterns"]:
                for pattern in angle["patterns"]:
                    lines.append(
                        f"\n#### {pattern['id']}: {pattern['name']} (Low-Level)"
                    )
                    lines.append(f"Definition: {pattern['definition']}")
                    lines.append(
                        f"Visual indicators: {pattern['visual_indicators']}"
                    )
                    lines.append(
                        f"Default severity: {pattern['severity_default']}"
                    )
            else:
                lines.append(
                    "(No sub-patterns — assess this angle directly at the meso level.)"
                )

    return "\n".join(lines)


OUTPUT_SCHEMA = """{
  "audit_metadata": {
    "url": "URL if provided, otherwise null",
    "page_type": "checkout | landing | settings | cookie_banner | product | pricing | signup | other",
    "audit_timestamp": "ISO 8601 timestamp",
    "ontology_version": "1.0"
  },
  "summary": {
    "total_findings": 0,
    "high": 0,
    "medium": 0,
    "low": 0,
    "risk_level": "High | Medium | Low | Clean"
  },
  "findings": [
    {
      "pattern_id": "e.g. S1.A1.P1 or S3.A2 for meso-level patterns without children",
      "pattern_name": "Name of the pattern",
      "strategy": "High-level strategy name",
      "angle": "Meso-level angle name",
      "severity": "High | Medium | Low",
      "evidence": "Start with [Screenshot], [HTML Source], or [Both] to indicate the source of this finding. Then describe what was observed — quote exact text, describe colors, sizes, placement. When the source is [HTML Source] or [Both], include the specific code snippet (e.g. the relevant HTML element or attribute) that confirms the finding, formatted as an inline code block.",
      "behavioural_mechanism": "Which cognitive bias or behavioural principle is being exploited",
      "harm_analysis": "Why this is deceptive and how it affects the user",
      "severity_justification": "Why this severity level was assigned",
      "recommendation": "What the interface should do instead",
      "regulatory_refs": ["e.g. EDPB: Skipping", "CMA: Choice Information", "DSA Art.25: Deception"]
    }
  ],
  "strategies_checked": {
    "Obstruction": { "checked": true, "findings_count": 0 },
    "Sneaking": { "checked": true, "findings_count": 0 },
    "Interface Interference": { "checked": true, "findings_count": 0 },
    "Forced Action": { "checked": true, "findings_count": 0 },
    "Social Engineering": { "checked": true, "findings_count": 0 }
  },
  "confidence_notes": "Any patterns you were uncertain about, with explanation of what additional information would help confirm or rule them out"
}"""


def build_system_prompt(ontology: dict) -> str:
    """Build the full system prompt with ontology, rubric, and instructions."""
    ontology_text = _format_ontology_for_prompt(ontology)

    return f"""You are a dark patterns screening tool for the Behavioural Insights Team (BIT). Your task is to systematically analyse a digital interface for deceptive design patterns ("dark patterns") and surface high-confidence detections for expert review.

You use a hybrid approach with the Gray et al. (2024) CHI Dark Patterns Ontology (version {ONTOLOGY_VERSION}) as the master classification schema — the most comprehensive academically validated framework, covering 65 patterns across 3 hierarchical levels. This is supplemented by operationalised definitions from Mathur et al. (2019) for text-based detection and regulatory mapping to EDPB, CMA, DSA, and FTC frameworks for jurisdiction-specific reporting.

# ONTOLOGY FRAMEWORK
{ontology_text}

# SEVERITY RUBRIC

Assign one of three severity levels to each finding:

**High**: Actively deceptive or coercive. The user is misled, financially harmed, or unable to exercise meaningful choice. The pattern exploits a cognitive vulnerability in a way that most users would not detect. Examples: hidden charges added silently, impossible account deletion, fabricated countdown timers, auto-opted-in paid services.

**Medium**: Manipulative but does not actively deceive. Steers user decisions through psychological pressure, visual design, or friction. An attentive user could recognise and overcome it. Examples: confirmshaming, false hierarchy between buttons, pressured selling during checkout, bad defaults on marketing consent.

**Low**: Nudge-like or borderline. Creates mild friction or pressure but does not cause direct financial or privacy harm. May be a common industry practice that is still worth flagging. Examples: nagging notifications, mild positive framing, choice overload in settings.

# ANALYSIS INSTRUCTIONS

1. **Check ALL 5 strategies systematically.** Do not skip any category. For each strategy, check every meso-level angle and every low-level pattern.

2. **For each detected pattern:**
   - Cite specific visual/textual evidence. **Prefix with [Screenshot], [HTML Source], or [Both]** to indicate which source the finding was drawn from. Quote exact text, describe colors, sizes, button labels, and spatial relationships. **When evidence comes from HTML, include the relevant code snippet** (e.g. `<input type="checkbox" checked name="marketing">`) so reviewers can locate it in the source.
   - Map to the ontology path (Strategy > Angle > Pattern).
   - Assign and justify the severity level.
   - Explain the behavioural mechanism being exploited (which cognitive bias or vulnerability).
   - Recommend a specific fix.

3. **For strategies with no findings:** Explicitly confirm they were checked in the strategies_checked field.

4. **Flag uncertainty:** If a pattern might be present but you cannot confirm from the screenshot alone, note it in confidence_notes. Explain what additional information would be needed.

5. **Use both the screenshot AND HTML source if provided.** The HTML source may reveal dark patterns not visible in the screenshot — e.g. pre-checked hidden inputs, deceptive `aria-label` attributes, `display:none` elements that may appear later, or manipulative JavaScript. Cite HTML evidence specifically when you use it.

6. **Do NOT over-flag.** Not every design choice is a dark pattern. Standard UX conventions (e.g., a prominent CTA button, a "Recommended" badge on a genuinely popular plan) are not inherently dark patterns unless combined with manipulative elements. Only flag patterns where there is clear evidence of manipulation, deception, or coercion.

7. **Consider context.** A countdown timer on a live auction is legitimate; a countdown timer on an always-available product is deceptive. Context matters for severity assignment.

8. **For meso-level patterns with no children** (e.g., Bad Defaults, Nagging, Forced Continuity), assess them directly and use the angle ID as the pattern_id.

9. **Map findings to regulatory frameworks.** For each finding, identify which regulatory frameworks are most relevant and populate the regulatory_refs field. Use the regulatory relevance noted in the ontology to connect findings to specific provisions:
   - **EDPB** (EU/GDPR): Overloading, Skipping, Stirring, Obstructing, Fickle, Left in the Dark
   - **CMA** (UK): Choice Structure, Choice Information, Choice Pressure
   - **DSA Art.25** (EU): Deception, Manipulation, Distortion/Impairment of Autonomy
   - **FTC** (US): Endorsements, Design tricks to mislead, Making it difficult to cancel, Burying key terms

10. **Enhanced text-pattern detection.** When analysing text content (from screenshots or HTML), apply Mathur et al.'s (2019) operationalised categories for common e-commerce dark patterns: urgency language ("Act now!", "Hurry!"), scarcity claims ("Only X left"), social proof claims ("Y people bought this"), misdirection through visual hierarchy, and confirmshaming on decline options. These text patterns are empirically validated with 97.5% accuracy on the Mathur et al. dataset.

11. **Screening tool positioning.** You are a screening and flagging tool, not a definitive classifier. Surface high-confidence detections with clear evidence. When uncertain, flag the pattern in confidence_notes rather than asserting it as a definitive finding. Your outputs are intended for expert review by BIT consultants and regulatory professionals.

# OUTPUT FORMAT

Return ONLY valid JSON matching this exact schema. Do not include any text before or after the JSON.

{OUTPUT_SCHEMA}

Ensure summary counts match the actual findings array. Set risk_level based on the highest severity found (High if any High findings, Medium if any Medium, Low if only Low, Clean if no findings)."""


def build_user_message(
    image_bytes: bytes,
    source_description: str,
    html_source: str | None = None,
) -> list:
    """Build the user message content array with image, instruction, and optional HTML."""
    image_b64 = base64.b64encode(image_bytes).decode("utf-8")

    # Detect media type from bytes
    media_type = "image/png"
    if image_bytes[:3] == b"\xff\xd8\xff":
        media_type = "image/jpeg"
    elif image_bytes[:4] == b"RIFF" and image_bytes[8:12] == b"WEBP":
        media_type = "image/webp"

    content = [
        {
            "type": "image",
            "source": {
                "type": "base64",
                "media_type": media_type,
                "data": image_b64,
            },
        },
        {
            "type": "text",
            "text": f"Audit this interface for dark patterns. Source: {source_description or 'Uploaded screenshot'}",
        },
    ]

    if html_source:
        # Cap at 50,000 characters to stay within token limits
        truncated = html_source[:50000]
        if len(html_source) > 50000:
            truncated += "\n<!-- [HTML truncated for length] -->"
        content.append({
            "type": "text",
            "text": f"HTML source code of the page:\n\n```html\n{truncated}\n```",
        })

    return content
