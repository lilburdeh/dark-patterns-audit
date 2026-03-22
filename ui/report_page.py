"""Report display page for the Dark Patterns Audit Tool."""

from __future__ import annotations

import re

import streamlit as st

from ui.components import severity_badge, risk_banner, metric_card, regulatory_tag, severity_chart


def _strip_ids(text: str) -> str:
    """Remove internal ontology IDs like (S2.A2.P3) or (S3.A2) from text."""
    return re.sub(r'\s*\(S\d+\.A\d+(?:\.P\d+)?\)', '', text)


def _escape_dollars(text: str) -> str:
    """Escape $ signs so Streamlit doesn't render LaTeX math."""
    return text.replace("$", "\\$")


def render_report(audit_result: dict, image_bytes: bytes | None = None) -> None:
    """Render the full audit report in Streamlit."""
    summary = audit_result.get("summary", {})
    findings = audit_result.get("findings", [])
    metadata = audit_result.get("audit_metadata", {})
    strategies_checked = audit_result.get("strategies_checked", {})
    confidence_notes = audit_result.get("confidence_notes", "")

    # --- New Audit button ---
    if st.button("New Audit", type="secondary"):
        st.session_state["current_result"] = None
        st.session_state["current_image"] = None
        st.session_state["source_type"] = ""
        st.session_state["source_description"] = ""
        st.session_state["html_source"] = None
        st.rerun()

    _, centre, _ = st.columns([1, 6, 1])
    with centre:

        # --- Executive Summary ---
        st.header("Executive Summary")

        # Risk level banner
        risk_level = summary.get("risk_level", "Clean")
        st.markdown(risk_banner(risk_level), unsafe_allow_html=True)

        # Metric cards as custom HTML
        total = summary.get("total_findings", 0)
        high = summary.get("high", 0)
        medium = summary.get("medium", 0)
        low = summary.get("low", 0)

        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(metric_card(
                high, "High Severity", "high",
                tooltip="Actively deceptive or coercive. User is misled, financially harmed, or unable to exercise meaningful choice.",
            ), unsafe_allow_html=True)
        with col2:
            st.markdown(metric_card(
                medium, "Medium Severity", "medium",
                tooltip="Manipulative but visible to attentive users. Steers decisions through psychological pressure or interface design.",
            ), unsafe_allow_html=True)
        with col3:
            st.markdown(metric_card(
                low, "Low Severity", "low",
                tooltip="Nudge-like or borderline. May not cause direct harm but creates friction or mild pressure.",
            ), unsafe_allow_html=True)

        # Severity chart
        if total > 0:
            st.plotly_chart(severity_chart(summary), use_container_width=True)

        # --- Limitations & Caveats callout ---
        if confidence_notes:
            notes_html = _strip_ids(confidence_notes).replace('\n', '<br>')
            st.markdown(
                f"<div style='"
                f"background:#F7F9FC;"
                f"border-left:4px solid #6B7280;"
                f"padding:14px 18px;"
                f"border-radius:0 6px 6px 0;"
                f"margin:16px 0 4px 0;"
                f"'>"
                f"<div style='font-weight:600;font-size:0.9rem;color:#374151;margin-bottom:6px;'>"
                f"Limitations &amp; Caveats</div>"
                f"<div style='font-size:0.9rem;color:#4B5563;line-height:1.6;'>{notes_html}</div>"
                f"</div>",
                unsafe_allow_html=True,
            )

        # --- Findings Table ---
        if findings:
            st.header("Findings Overview")

            rows_html = ""
            for i, f in enumerate(findings):
                rows_html += (
                    f"<tr>"
                    f"<td style='padding:8px 6px;border-bottom:1px solid #e8e8e8;vertical-align:top;color:#6B7280;font-size:0.8rem;'>{i + 1}</td>"
                    f"<td style='padding:8px 6px;border-bottom:1px solid #e8e8e8;vertical-align:top;font-weight:500;'>{f.get('pattern_name', '')}</td>"
                    f"<td style='padding:8px 6px;border-bottom:1px solid #e8e8e8;vertical-align:top;'>{f.get('severity', '')}</td>"
                    f"<td style='padding:8px 6px;border-bottom:1px solid #e8e8e8;vertical-align:top;'>{f.get('evidence', '')}</td>"
                    f"</tr>"
                )
            table_html = (
                "<table style='width:100%;border-collapse:collapse;font-size:0.9rem;'>"
                "<thead><tr style='border-bottom:2px solid #d0d0d0;background:rgba(0,0,0,0.02);'>"
                "<th style='text-align:left;padding:8px 6px;width:3%;'>#</th>"
                "<th style='text-align:left;padding:8px 6px;width:18%;'>Pattern</th>"
                "<th style='text-align:left;padding:8px 6px;width:9%;'>Severity</th>"
                "<th style='text-align:left;padding:8px 6px;width:70%;'>Evidence</th>"
                "</tr></thead>"
                f"<tbody>{rows_html}</tbody>"
                "</table>"
            )
            st.markdown(table_html, unsafe_allow_html=True)

        # --- Detailed Findings ---
        if findings:
            st.header("Detailed Findings")

            for i, finding in enumerate(findings):
                severity = finding.get("severity", "")
                pattern_name = finding.get("pattern_name", "Unknown")

                with st.expander(
                    f"Finding {i + 1}: {pattern_name} ({severity})", expanded=False
                ):
                    # Ontology path + severity badge
                    strategy = finding.get("strategy", "")
                    angle = finding.get("angle", "")
                    st.markdown(
                        f"**Ontology path:** {_escape_dollars(strategy)} > {_escape_dollars(angle)} > {_escape_dollars(pattern_name)} "
                        f"&nbsp;&nbsp; {severity_badge(severity)}",
                        unsafe_allow_html=True,
                    )
                    st.markdown("")

                    # Evidence
                    _finding_section("Evidence", finding.get("evidence", "No evidence provided."))

                    # Behavioural mechanism
                    _finding_section("Behavioural Mechanism", finding.get("behavioural_mechanism", ""))

                    # Harm analysis
                    _finding_section("Why This Is a Dark Pattern", finding.get("harm_analysis", ""))

                    # Severity justification
                    _finding_section("Severity Justification", finding.get("severity_justification", ""))

                    # Recommendation
                    _finding_section("Recommendation", finding.get("recommendation", ""))

                    # Regulatory references
                    reg_refs = finding.get("regulatory_refs", [])
                    if reg_refs:
                        tags_html = " ".join(regulatory_tag(ref) for ref in reg_refs)
                        st.markdown(
                            f'<div class="finding-section">'
                            f'<div class="finding-section-label">Regulatory Relevance</div>'
                            f'{tags_html}</div>',
                            unsafe_allow_html=True,
                        )

        # --- Export ---
        st.header("Export")
        _render_export_buttons(audit_result, image_bytes)

    # --- Methodology (full-width, outside centred column) ---
    st.divider()
    with st.expander("Methodology", expanded=False):
        st.markdown(
            "**Primary framework:** Gray, C. M., Santos, C., Bielova, N., & Mildner, T. (2024). "
            "*An Ontology of Dark Patterns Knowledge.* "
            "CHI '24, ACM. — 65 patterns across 3 hierarchical levels."
        )
        st.markdown(
            "**Supplementary sources:** Mathur et al. (2019) operationalised definitions "
            "for text-based detection; EDPB Guidelines 03/2022, CMA Online Choice Architecture "
            "(2022), EU DSA Article 25, and FTC Dark Patterns Report (2022) for "
            "regulatory mapping."
        )
        st.markdown(
            f"**Ontology version:** {metadata.get('ontology_version', '1.0')}"
        )
        st.markdown(
            f"**Model:** {metadata.get('model', 'Claude')}"
        )
        st.markdown(
            "**Severity rubric:**\n"
            "- **High** — Actively deceptive or coercive. User is misled, "
            "financially harmed, or unable to exercise meaningful choice.\n"
            "- **Medium** — Manipulative but visible to attentive users. "
            "Steers decisions through psychological pressure or interface design.\n"
            "- **Low** — Nudge-like or borderline. Mild friction or pressure "
            "without direct harm."
        )
        st.markdown(
            "**Scope:** Static screenshot analysis. Multi-step flows were not tested."
        )
        st.markdown(
            "**Screening disclaimer:** This tool is a screening and flagging system "
            "that surfaces high-confidence detections for expert review. Findings are "
            "not definitive classifications. Results should be verified by a qualified "
            "reviewer before use in enforcement or compliance proceedings."
        )


def _finding_section(label: str, content: str) -> None:
    """Render a labelled section within a finding card."""
    if not content:
        return
    st.markdown(
        f'<div class="finding-section">'
        f'<div class="finding-section-label">{label}</div>'
        f'</div>',
        unsafe_allow_html=True,
    )
    st.markdown(_escape_dollars(_strip_ids(content)))



def _render_export_buttons(
    audit_result: dict, image_bytes: bytes | None = None
) -> None:
    """Render export download buttons."""
    col1, col2 = st.columns(2)

    with col1:
        try:
            from export.markdown_export import generate_markdown_report

            md_report = generate_markdown_report(audit_result, image_bytes)
            metadata = audit_result.get("audit_metadata", {})
            filename = _make_filename(metadata, "md")
            st.download_button(
                "Download Markdown",
                data=md_report,
                file_name=filename,
                mime="text/markdown",
                use_container_width=True,
            )
        except Exception as e:
            st.button("Download Markdown", disabled=True, use_container_width=True)
            st.caption(f"Export error: {e}")

    with col2:
        try:
            from export.pdf_export import generate_pdf_report

            pdf_bytes = generate_pdf_report(audit_result, image_bytes)
            metadata = audit_result.get("audit_metadata", {})
            filename = _make_filename(metadata, "pdf")
            st.download_button(
                "Download PDF",
                data=pdf_bytes,
                file_name=filename,
                mime="application/pdf",
                use_container_width=True,
            )
        except Exception as e:
            st.button("Download PDF", disabled=True, use_container_width=True)
            st.caption(f"Export error: {e}")


def _make_filename(metadata: dict, ext: str) -> str:
    """Generate a filename from audit metadata."""
    url = metadata.get("url", "")
    timestamp = metadata.get("audit_timestamp", "")

    if url:
        from urllib.parse import urlparse
        domain = urlparse(url).netloc.replace("www.", "").replace(".", "-")
        slug = domain[:30]
    else:
        slug = "screenshot"

    date_part = timestamp[:10] if timestamp else "undated"
    return f"audit-{slug}-{date_part}.{ext}"
