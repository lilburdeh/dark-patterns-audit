"""Generate PDF audit reports using fpdf2."""

from __future__ import annotations

import re
from datetime import datetime

from fpdf import FPDF

from config.settings import SEVERITY_COLORS, REPORT_FOOTER


def _strip_ids(text: str) -> str:
    """Remove internal ontology IDs like (S2.A2.P3) or (S3.A2) from text."""
    return re.sub(r'\s*\(S\d+\.A\d+(?:\.P\d+)?\)', '', text)


def _sanitize(text: str) -> str:
    """Replace Unicode characters that Helvetica can't render."""
    replacements = {
        "\u2014": "--",   # em dash
        "\u2013": "-",    # en dash
        "\u2018": "'",    # left single quote
        "\u2019": "'",    # right single quote
        "\u201c": '"',    # left double quote
        "\u201d": '"',    # right double quote
        "\u2026": "...",  # ellipsis
        "\u2022": "-",    # bullet
    }
    for orig, repl in replacements.items():
        text = text.replace(orig, repl)
    return text


class AuditPDF(FPDF):
    """Custom PDF class for audit reports with Unicode sanitization."""

    def cell(self, w=0, h=None, text="", **kwargs):
        return super().cell(w, h, _sanitize(str(text)), **kwargs)

    def multi_cell(self, w, h=None, text="", **kwargs):
        return super().multi_cell(w, h, _sanitize(str(text)), **kwargs)

    def header(self):
        self.set_font("Helvetica", "B", 10)
        self.set_text_color(0, 0, 255)  # #0000FF brand blue
        super().cell(0, 8, "Dark Patterns Audit Report", align="L")
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(150, 150, 150)
        super().cell(0, 10, f"{REPORT_FOOTER}  |  Page {self.page_no()}", align="C")


def _hex_to_rgb(hex_color: str) -> tuple[int, int, int]:
    """Convert hex color to RGB tuple."""
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i : i + 2], 16) for i in (0, 2, 4))


def _add_severity_badge(pdf: FPDF, severity: str) -> None:
    """Add a colored severity badge inline."""
    color = SEVERITY_COLORS.get(severity, "#6B7280")
    r, g, b = _hex_to_rgb(color)
    pdf.set_fill_color(r, g, b)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("Helvetica", "B", 9)
    w = pdf.get_string_width(severity) + 8
    pdf.cell(w, 6, severity, fill=True, align="C")
    pdf.set_text_color(0, 0, 0)


def _clip_text(pdf: FPDF, text: str, width: float, padding: float = 2.0) -> str:
    """Truncate text with ellipsis to fit within width mm."""
    if pdf.get_string_width(text) <= width - padding:
        return text
    while len(text) > 0 and pdf.get_string_width(text + "...") > width - padding:
        text = text[:-1]
    return text + "..." if text else ""


def _bullet_item(pdf: FPDF, text: str, line_h: int = 6) -> None:
    """Draw a bullet point with hanging indent using middle dot (Latin-1 chr 183)."""
    bullet_w = 5
    text_w = pdf.w - pdf.l_margin - pdf.r_margin - bullet_w
    pdf.set_x(pdf.l_margin)
    pdf.cell(bullet_w, line_h, chr(183), ln=0)  # · middle dot, in Latin-1
    pdf.multi_cell(text_w, line_h, text)


def generate_pdf_report(audit_result: dict, image_bytes: bytes | None = None) -> bytes:
    """Generate a PDF report from an audit result dict.

    Returns PDF content as bytes.
    """
    metadata = audit_result.get("audit_metadata", {})
    summary = audit_result.get("summary", {})
    findings = audit_result.get("findings", [])
    confidence_notes = audit_result.get("confidence_notes", "")

    pdf = AuditPDF()
    pdf.set_auto_page_break(auto=True, margin=20)
    pdf.add_page()

    # --- Title (Level 1 — core blue) ---
    pdf.set_font("Helvetica", "B", 22)
    pdf.set_text_color(0, 0, 255)  # #0000FF brand blue — Level 1 only
    pdf.cell(0, 14, "Dark Patterns Audit Report", ln=True)
    pdf.ln(4)

    # --- Metadata ---
    raw_ts = metadata.get("audit_timestamp", datetime.now().isoformat())
    tz_str = datetime.now().astimezone().strftime("%Z")
    date_str = (raw_ts[:16].replace("T", " ") + f" {tz_str}") if len(raw_ts) > 10 else raw_ts
    url = metadata.get("url", "")
    source = url if url else "Uploaded screenshot"

    pdf.set_font("Helvetica", "", 11)
    pdf.set_text_color(80, 80, 80)
    meta_lines = [
        f"Date and time: {date_str}",
        f"Source: {source}",
        f"Analyst: Automated — {metadata.get('model', 'Claude')}",
    ]
    for line in meta_lines:
        pdf.cell(0, 6, line, ln=True)
    pdf.ln(6)

    # --- Executive Summary ---
    pdf.set_font("Helvetica", "B", 16)
    pdf.set_text_color(0, 0, 0)  # black — Level 2+
    pdf.cell(0, 10, "Executive Summary", ln=True)
    pdf.ln(2)

    # Risk level
    risk_level = summary.get("risk_level", "Clean")
    pdf.set_font("Helvetica", "B", 11)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(30, 8, "Risk Level: ")
    _add_severity_badge(pdf, risk_level)
    pdf.ln(12)

    # Summary counts
    pdf.set_font("Helvetica", "", 11)
    pdf.set_text_color(0, 0, 0)
    total = summary.get("total_findings", 0)
    high = summary.get("high", 0)
    medium = summary.get("medium", 0)
    low = summary.get("low", 0)

    pdf.cell(0, 6, f"Total findings: {total}", ln=True)
    pdf.cell(0, 6, f"  High: {high}  |  Medium: {medium}  |  Low: {low}", ln=True)
    pdf.ln(4)

    # Limitations & Caveats
    if confidence_notes:
        pdf.set_font("Helvetica", "B", 11)
        pdf.set_text_color(0, 0, 0)
        pdf.cell(0, 6, "Limitations & Caveats:", ln=True)
        pdf.set_font("Helvetica", "", 11)
        pdf.multi_cell(0, 6, _strip_ids(confidence_notes))
        pdf.ln(4)
    else:
        pdf.ln(2)

    # --- Findings Table ---
    if findings:
        pdf.set_font("Helvetica", "B", 16)
        pdf.set_text_color(0, 0, 0)  # black
        pdf.cell(0, 10, "Findings Overview", ln=True)
        pdf.ln(2)

        # Table header — total page width ~190mm at A4 with margins
        col_widths = [8, 42, 38, 18, 84]
        headers = ["#", "Pattern", "Category", "Severity", "Evidence"]

        pdf.set_font("Helvetica", "B", 9)
        pdf.set_text_color(0, 0, 0)  # black text in table headers
        pdf.set_fill_color(247, 239, 222)  # #F7EFDE brand stone
        for i, header in enumerate(headers):
            pdf.cell(col_widths[i], 7, header, border=1, fill=True)
        pdf.ln()

        # Table rows — use multi_cell for Evidence so text wraps
        pdf.set_font("Helvetica", "", 8)
        pdf.set_text_color(0, 0, 0)  # black text in table rows
        for i, f in enumerate(findings):
            evidence = _strip_ids(f.get("evidence", ""))
            strategy = f.get("strategy", "")
            angle = f.get("angle", "")
            category = f"{strategy} > {angle}"

            # Calculate row height based on evidence length
            evidence_lines = max(1, len(evidence) // 55 + 1)
            row_h = max(7, evidence_lines * 5)

            x_start = pdf.get_x()
            y_start = pdf.get_y()

            # Check page break before drawing row
            if y_start + row_h > pdf.page_break_trigger:
                pdf.add_page()
                y_start = pdf.get_y()

            # Clip text to prevent overflow into adjacent cells
            cells = [
                (col_widths[0], str(i + 1)),
                (col_widths[1], _clip_text(pdf, f.get("pattern_name", ""), col_widths[1])),
                (col_widths[2], _clip_text(pdf, category, col_widths[2])),
                (col_widths[3], f.get("severity", "")),
            ]
            for w, val in cells:
                pdf.cell(w, row_h, val, border=1, align="L")

            # Evidence with wrapping
            pdf.multi_cell(col_widths[4], 5, evidence, border=1)

            # Ensure next row starts after the tallest cell
            pdf.set_xy(x_start, y_start + row_h)

        pdf.ln(6)

    # --- Detailed Findings ---
    if findings:
        pdf.set_font("Helvetica", "B", 16)
        pdf.set_text_color(0, 0, 0)  # black
        pdf.cell(0, 10, "Detailed Findings", ln=True)
        pdf.ln(2)

        for i, f in enumerate(findings):
            # Check if we need a new page
            if pdf.get_y() > 230:
                pdf.add_page()

            pattern_name = f.get("pattern_name", "Unknown")
            severity = f.get("severity", "")
            strategy = f.get("strategy", "")
            angle = f.get("angle", "")

            # Finding header — explicitly black (would otherwise inherit blue from section header)
            pdf.set_font("Helvetica", "B", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(0, 8, f"Finding {i + 1}: {pattern_name}", ln=True)

            # Classification
            pdf.set_font("Helvetica", "", 9)
            pdf.set_text_color(80, 80, 80)
            pdf.cell(0, 5, f"Classification: {strategy} > {angle} > {pattern_name}", ln=True)

            # Severity
            pdf.set_text_color(0, 0, 0)
            pdf.cell(20, 6, "Severity: ")
            _add_severity_badge(pdf, severity)
            pdf.ln(8)

            # Content sections
            pdf.set_text_color(0, 0, 0)
            sections = [
                ("Evidence", _strip_ids(f.get("evidence", ""))),
                ("Behavioural mechanism", _strip_ids(f.get("behavioural_mechanism", ""))),
                ("Why this is a dark pattern", _strip_ids(f.get("harm_analysis", ""))),
                ("Severity justification", _strip_ids(f.get("severity_justification", ""))),
                ("Recommendation", _strip_ids(f.get("recommendation", ""))),
            ]

            for label, content in sections:
                if content:
                    pdf.set_font("Helvetica", "B", 11)
                    pdf.cell(0, 6, f"{label}:", ln=True)
                    pdf.set_font("Helvetica", "", 11)
                    pdf.multi_cell(0, 6, content)
                    pdf.ln(2)

            # Regulatory refs
            reg_refs = f.get("regulatory_refs", [])
            if reg_refs:
                pdf.set_font("Helvetica", "B", 11)
                pdf.cell(0, 6, "Regulatory relevance:", ln=True)
                pdf.set_font("Helvetica", "", 11)
                pdf.multi_cell(0, 6, ", ".join(reg_refs))
                pdf.ln(2)

            pdf.ln(4)

    # --- Methodology ---
    if pdf.get_y() > 220:
        pdf.add_page()

    pdf.set_font("Helvetica", "B", 16)
    pdf.set_text_color(0, 0, 0)  # black
    pdf.cell(0, 10, "Methodology", ln=True)
    pdf.ln(2)

    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Helvetica", "B", 11)
    pdf.cell(0, 6, "Primary framework:", ln=True)
    pdf.set_font("Helvetica", "", 11)
    pdf.multi_cell(
        0,
        6,
        "Gray, C. M., Santos, C., Bielova, N., & Mildner, T. (2024). "
        "An Ontology of Dark Patterns Knowledge. Proceedings of the CHI "
        "Conference on Human Factors in Computing Systems (CHI '24), ACM. "
        "A three-level taxonomy: 5 high-level strategies, 25 meso-level "
        "angles of attack, and 35 low-level patterns (65 total).",
    )
    pdf.ln(2)

    pdf.set_font("Helvetica", "B", 11)
    pdf.cell(0, 6, "Supplementary sources:", ln=True)
    pdf.set_font("Helvetica", "", 11)
    pdf.multi_cell(
        0,
        6,
        "Mathur et al. (2019) for text-based detection; EDPB Guidelines 03/2022, "
        "CMA Online Choice Architecture (2022), EU DSA Article 25, and FTC Dark "
        "Patterns Report (2022) for regulatory mapping.",
    )
    pdf.ln(2)

    pdf.set_font("Helvetica", "B", 11)
    pdf.cell(0, 6, "Severity Rubric:", ln=True)
    pdf.set_font("Helvetica", "", 11)
    rubric = [
        "High: Actively deceptive or coercive. User is misled, financially harmed, or unable to exercise meaningful choice.",
        "Medium: Manipulative but visible to attentive users. Steers decisions through psychological pressure or interface design.",
        "Low: Nudge-like or borderline. May not cause direct harm but creates friction or mild pressure.",
    ]
    for line in rubric:
        _bullet_item(pdf, line)
    pdf.ln(2)

    pdf.set_font("Helvetica", "", 11)
    pdf.cell(0, 6, "Scope: Static screenshot analysis", ln=True)
    pdf.ln(2)
    pdf.set_font("Helvetica", "B", 11)
    pdf.cell(0, 6, "Screening disclaimer:", ln=True)
    pdf.set_font("Helvetica", "", 11)
    pdf.multi_cell(
        0,
        6,
        "This tool is a screening and flagging system that surfaces high-confidence "
        "detections for expert review. Findings are not definitive classifications. "
        "Results should be verified by a qualified reviewer before use in enforcement "
        "or compliance proceedings.",
    )

    # --- Screenshot ---
    if image_bytes:
        from io import BytesIO
        pdf.add_page()
        pdf.set_font("Helvetica", "B", 16)
        pdf.set_text_color(0, 0, 0)  # black
        pdf.cell(0, 10, "Screenshot", ln=True)
        pdf.ln(2)
        pdf.set_font("Helvetica", "", 11)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(0, 6, "Captured at time of audit for reference.", ln=True)
        pdf.ln(4)
        pdf.image(BytesIO(image_bytes), x=10, w=pdf.w - 20)

    return bytes(pdf.output())
