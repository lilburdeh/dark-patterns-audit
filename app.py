"""Dark Patterns Audit Tool — Main Streamlit Application."""

from pathlib import Path
from dotenv import load_dotenv
load_dotenv(Path(__file__).parent / ".env", override=True)

import streamlit as st

from config.settings import APP_TITLE, get_api_key
from ui.input_page import render_input_section
from ui.report_page import render_report
from ui.styles import get_custom_css
from core.analyser import run_audit

# --- Page config ---
st.set_page_config(
    page_title=APP_TITLE,
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- Inject custom CSS ---
st.markdown(get_custom_css(), unsafe_allow_html=True)

# --- Session state initialization ---
if "audit_history" not in st.session_state:
    st.session_state["audit_history"] = []
if "current_result" not in st.session_state:
    st.session_state["current_result"] = None
if "current_image" not in st.session_state:
    st.session_state["current_image"] = None
if "html_source" not in st.session_state:
    st.session_state["html_source"] = None

# --- Sidebar ---
with st.sidebar:
    # Title
    st.markdown(
        '<div style="font-size:2rem;font-weight:700;margin:0px 0px 0.25rem;letter-spacing:0;color:#0000FF;">'
        'Dark Patterns Audit Tool</div>',
        unsafe_allow_html=True,
    )
    st.caption("Built by Sai Ming (BIT Singapore)")

    st.divider()

    # About
    st.markdown(
        "This tool screens websites and digital interfaces for **dark patterns** "
        "— deceptive design techniques that manipulate users into unintended actions.\n\n"
        "Upload a screenshot or enter a URL, and the tool will produce a structured "
        "audit report covering:\n"
        "- Detected patterns mapped to an academic ontology\n"
        "- Severity ratings\n"
        "- Behavioural harm analysis\n"
        "- Regulatory relevance\n"
        "- Recommended fixes"
    )

    st.divider()

    # Frameworks — collapsible with links
    with st.expander("Frameworks & Sources"):
        st.markdown(
            "**Primary framework:**\n\n"
            "- [Gray et al. (2024) — An Ontology of Dark Patterns Knowledge](https://doi.org/10.1145/3613904.3642436) "
            "(CHI '24) — 65 patterns, 3 levels\n\n"
            "**Text-based detection:**\n\n"
            "- [Mathur et al. (2019) — Dark Patterns at Scale](https://doi.org/10.1145/3359183) "
            "(CSCW '19) — 15 types, 11K sites crawled\n\n"
            "**Regulatory frameworks:**\n\n"
            "- [EDPB Guidelines 03/2022](https://edpb.europa.eu/our-work-tools/documents/public-consultations/2022/guidelines-032022-deceptive-design-patterns_en) "
            "— EU/GDPR\n"
            "- [CMA Online Choice Architecture](https://www.gov.uk/government/publications/online-choice-architecture-how-digital-design-can-harm-competition-and-consumers) "
            "— UK\n"
            "- [EU Digital Services Act, Art. 25](https://eur-lex.europa.eu/eli/reg/2022/2065/oj) "
            "— EU\n"
            "- [FTC: Bringing Dark Patterns to Light](https://www.ftc.gov/reports/bringing-dark-patterns-light) "
            "— US"
        )

    # Audit history
    if st.session_state["audit_history"]:
        st.divider()
        st.markdown(
            '<p style="font-size:0.85rem;font-weight:600;margin-bottom:0.5rem;">Audit History</p>',
            unsafe_allow_html=True,
        )
        for i, audit in enumerate(reversed(st.session_state["audit_history"])):
            emoji = "🌐" if audit.get("source_type") == "url" else "🖼️"
            if st.button(
                f"{emoji} {audit['label']}",
                key=f"history_{i}",
                use_container_width=True,
            ):
                st.session_state["current_result"] = audit["result"]
                st.session_state["current_image"] = audit.get("image")
                st.rerun()

# --- Instruction callout ---
st.markdown(
    '<div style="background-color:#97D9E3;color:#000000;padding:1rem 1.5rem;border-radius:10px;'
    'margin-bottom:1.5rem;line-height:1.6;max-width:50%;margin-left:auto;margin-right:auto;'
    'text-align:center;font-size:1rem;">'
    '<strong>Upload a screenshot or enter a URL below, then click Run Audit.</strong>'
    '</div>',
    unsafe_allow_html=True,
)

# Check API key
api_key = get_api_key()
if not api_key:
    st.warning(
        "No Anthropic API key found. Set `ANTHROPIC_API_KEY` in your `.env` file.",
        icon="🔑",
    )

# Input section
image_bytes, source_type, source_description = render_input_section()

# Run audit
if st.session_state.get("run_audit") and image_bytes and api_key:
    st.session_state["run_audit"] = False

    with st.spinner("Analysing for dark patterns — this takes about 30 seconds..."):
        try:
            result = run_audit(
                image_bytes,
                source_type,
                source_description,
                html_source=st.session_state.get("html_source"),
            )
            st.session_state["current_result"] = result
            st.session_state["current_image"] = image_bytes

            from datetime import datetime
            st.session_state["audit_history"].append({
                "label": (source_description or "Uploaded screenshot")[:50],
                "source_type": source_type,
                "timestamp": datetime.now().isoformat(),
                "result": result,
                "image": image_bytes,
            })
        except Exception as e:
            st.error(f"Analysis failed: {e}")

# Display report
if st.session_state["current_result"]:
    render_report(
        st.session_state["current_result"],
        st.session_state.get("current_image"),
    )
