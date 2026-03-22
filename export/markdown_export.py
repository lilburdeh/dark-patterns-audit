"""Generate markdown audit reports matching the report template."""

from __future__ import annotations

import base64
from datetime import datetime


def generate_markdown_report(
    audit_result: dict, image_bytes: bytes | None = None
) -> str:
    """Generate a markdown report from an audit result dict.

    Follows the template from references/report-template.md.
    """
    metadata = audit_result.get("audit_metadata", {})
    summary = audit_result.get("summary", {})
    findings = audit_result.get("findings", [])
    confidence_notes = audit_result.get("confidence_notes", "")

    lines = []

    # Title
    lines.append("# Dark Patterns Audit Report")
    lines.append("")

    # Audit Metadata
    lines.append("## Audit Metadata")
    lines.append("")
    lines.append("| Field | Value |")
    lines.append("|-------|-------|")
    raw_ts = metadata.get("audit_timestamp", datetime.now().isoformat())
    date_time_str = raw_ts[:16].replace("T", " ") if len(raw_ts) > 10 else raw_ts
    lines.append(f"| **Date and time** | {date_time_str} |")
    url = metadata.get("url")
    source_type = "URL" if url else "Screenshot"
    lines.append(f"| **Source** | {source_type} |")
    source_desc = url if url else "Uploaded screenshot"
    lines.append(f"| **Source Description** | {source_desc} |")
    lines.append(
        "| **Framework** | Gray et al. (2024) An Ontology of Dark Patterns Knowledge (CHI '24) |"
    )
    lines.append("| **Analyst** | Automated — Claude |")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Executive Summary
    lines.append("## Executive Summary")
    lines.append("")
    lines.append(f"**Overall Risk:** {summary.get('risk_level', 'Clean')}")
    lines.append("")
    lines.append("| Severity | Count |")
    lines.append("|----------|-------|")
    lines.append(f"| High | {summary.get('high', 0)} |")
    lines.append(f"| Medium | {summary.get('medium', 0)} |")
    lines.append(f"| Low | {summary.get('low', 0)} |")
    lines.append("")

    # Analyst Notes in Executive Summary (bullet points)
    if confidence_notes:
        lines.append("**Analyst Notes**")
        lines.append("")
        sentences = [
            s.strip()
            for s in confidence_notes.replace(". ", ".|").split("|")
            if s.strip()
        ]
        for s in sentences:
            lines.append(f"- {s if s.endswith('.') else s + '.'}")
        lines.append("")

    lines.append("---")
    lines.append("")

    # Findings Overview
    lines.append("## Findings Overview")
    lines.append("")
    lines.append(
        "| # | Pattern | Strategy | Angle | Severity | Evidence |"
    )
    lines.append(
        "|---|---------|----------|-------|----------|----------|"
    )
    for i, f in enumerate(findings):
        evidence = f.get("evidence", "")
        lines.append(
            f"| {i + 1} | {f.get('pattern_name', '')} | "
            f"{f.get('strategy', '')} | {f.get('angle', '')} | "
            f"{f.get('severity', '')} | {evidence} |"
        )
    lines.append("")
    lines.append("---")
    lines.append("")

    # Detailed Findings
    lines.append("## Detailed Findings")
    lines.append("")
    for i, f in enumerate(findings):
        pattern_name = f.get("pattern_name", "Unknown")
        strategy = f.get("strategy", "")
        angle = f.get("angle", "")
        severity = f.get("severity", "")

        lines.append(f"### Finding {i + 1}: {pattern_name}")
        lines.append("")
        lines.append("| Field | Value |")
        lines.append("|-------|-------|")
        lines.append(
            f"| **Ontology Classification** | {strategy} > {angle} > {pattern_name} |"
        )
        lines.append(f"| **Severity** | {severity} |")
        lines.append("")

        lines.append("**Evidence:**")
        lines.append(f.get("evidence", "No evidence provided."))
        lines.append("")

        mechanism = f.get("behavioural_mechanism", "")
        if mechanism:
            lines.append("**Behavioural mechanism:**")
            lines.append(mechanism)
            lines.append("")

        harm = f.get("harm_analysis", "")
        if harm:
            lines.append("**Why this is a dark pattern:**")
            lines.append(harm)
            lines.append("")

        justification = f.get("severity_justification", "")
        if justification:
            lines.append("**Severity justification:**")
            lines.append(justification)
            lines.append("")

        recommendation = f.get("recommendation", "")
        if recommendation:
            lines.append("**Recommendation:**")
            lines.append(recommendation)
            lines.append("")

        reg_refs = f.get("regulatory_refs", [])
        if reg_refs:
            lines.append("**Regulatory relevance:**")
            lines.append(", ".join(reg_refs))
            lines.append("")

        lines.append("---")
        lines.append("")

    # Methodology
    lines.append("## Methodology")
    lines.append("")
    lines.append(
        "**Primary framework:** Gray, C. M., Santos, C., Bielova, N., & Mildner, T. (2024). "
        "*An Ontology of Dark Patterns Knowledge.* Proceedings of the CHI Conference on "
        "Human Factors in Computing Systems (CHI '24), ACM. A three-level taxonomy: "
        "5 high-level strategies, 25 meso-level angles of attack, and 35 low-level "
        "patterns (65 total)."
    )
    lines.append("")
    lines.append(
        "**Supplementary sources:** Mathur et al. (2019) operationalised definitions "
        "for text-based detection; EDPB Guidelines 03/2022, CMA Online Choice Architecture "
        "(2022), EU DSA Article 25, and FTC Dark Patterns Report (2022) for "
        "regulatory mapping."
    )
    lines.append("")
    lines.append("**Severity Rubric:**")
    lines.append(
        "- **High**: Actively deceptive or coercive. User is misled, financially harmed, "
        "or unable to exercise meaningful choice."
    )
    lines.append(
        "- **Medium**: Manipulative but does not actively hide information. Steers user "
        "decisions through psychological pressure or interface design."
    )
    lines.append(
        "- **Low**: Nudge-like or borderline. May not cause direct harm but creates "
        "friction or mild pressure."
    )
    lines.append("")
    lines.append("**Scope:** Static screenshot analysis")
    lines.append("")
    lines.append(
        "**Screening disclaimer:** This tool is a screening and flagging system "
        "that surfaces high-confidence detections for expert review. Findings are "
        "not definitive classifications. Results should be verified by a qualified "
        "reviewer before use in enforcement or compliance proceedings."
    )
    lines.append("")

    # Screenshot at the bottom
    if image_bytes:
        lines.append("---")
        lines.append("")
        lines.append("## Screenshot")
        lines.append("")
        b64 = base64.b64encode(image_bytes).decode()
        lines.append(f"![Audited screenshot](data:image/png;base64,{b64})")
        lines.append("")

    return "\n".join(lines)
