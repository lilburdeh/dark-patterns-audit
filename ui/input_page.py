"""Input section for the Dark Patterns Audit Tool."""

from __future__ import annotations

import streamlit as st

from config.settings import ALLOWED_IMAGE_TYPES
from core.screenshot import is_playwright_available, capture_url


def render_input_section() -> tuple[bytes | None, str, str]:
    """Render the input section and return (image_bytes, source_type, source_description).

    Returns (None, "", "") if no input is ready.
    """
    # Restore from session state in case of rerun after URL capture
    image_bytes = st.session_state.get("current_image")
    source_type = st.session_state.get("source_type", "")
    source_description = st.session_state.get("source_description", "")

    # Centre the input area
    _, centre, _ = st.columns([1, 2, 1])

    with centre:
        # --- Screenshot upload ---
        st.markdown(
            '<p style="font-size:1.2rem;font-weight:600;margin-bottom:0.25rem;">'
            'Upload a screenshot</p>'
            '<p style="font-size:1rem;color:#000;opacity:0.6;margin-bottom:0.5rem;">'
            'Drag and drop or click to upload a screenshot (PNG, JPG, WEBP)</p>',
            unsafe_allow_html=True,
        )
        uploaded_file = st.file_uploader(
            "Upload a screenshot",
            type=ALLOWED_IMAGE_TYPES,
            label_visibility="collapsed",
        )
        if uploaded_file is not None:
            image_bytes = uploaded_file.getvalue()
            source_type = "screenshot"
            source_description = uploaded_file.name
            st.session_state["current_image"] = image_bytes
            st.session_state["source_type"] = source_type
            st.session_state["source_description"] = source_description

        # --- Divider ---
        st.markdown(
            '<div style="display:flex;align-items:center;margin:0.75rem 0;">'
            '<div style="flex:1;height:1px;background:#E8DFD0;"></div>'
            '<span style="padding:0 1rem;color:#000;opacity:0.4;font-size:0.95rem;font-weight:600;">OR</span>'
            '<div style="flex:1;height:1px;background:#E8DFD0;"></div>'
            '</div>',
            unsafe_allow_html=True,
        )

        # --- URL capture ---
        playwright_available = is_playwright_available()
        st.markdown(
            '<p style="font-size:1.2rem;font-weight:600;margin-bottom:0.25rem;">'
            'Enter a URL</p>'
            '<p style="font-size:1rem;color:#000;opacity:0.6;margin-bottom:0.5rem;">'
            + (
                'Enter a URL to automatically capture a screenshot and HTML source for analysis.'
                if playwright_available
                else 'URL capture requires Playwright. Please upload a screenshot instead.'
            )
            + '</p>',
            unsafe_allow_html=True,
        )
        url = st.text_input(
            "Enter a URL",
            placeholder="https://example.com",
            disabled=not playwright_available,
            label_visibility="collapsed",
        )

        if url and playwright_available and not uploaded_file:
            if st.button("Capture screenshot and page source", use_container_width=True):
                with st.spinner("Capturing screenshot and page source..."):
                    screenshot, html = capture_url(url)
                    if screenshot:
                        image_bytes = screenshot
                        source_type = "url"
                        source_description = url
                        st.session_state["current_image"] = image_bytes
                        st.session_state["source_type"] = source_type
                        st.session_state["source_description"] = source_description
                        st.session_state["html_source"] = html
                    else:
                        st.error(
                            "Failed to capture screenshot. "
                            "Please upload a screenshot manually."
                        )

    # --- Run Audit button (centred) ---
    _, centre2, _ = st.columns([1, 2, 1])
    with centre2:
        if image_bytes:
            st.markdown("")
            if st.session_state.get("html_source"):
                st.success("Screenshot and page source ready for analysis.")
            else:
                st.success("Screenshot ready for analysis.")
            if st.button("Run Audit", type="primary", use_container_width=True):
                st.session_state["run_audit"] = True
                st.rerun()

    # Return current values (including from session state for rerun)
    if st.session_state.get("run_audit"):
        return (
            st.session_state.get("current_image"),
            st.session_state.get("source_type", "screenshot"),
            st.session_state.get("source_description", ""),
        )

    return None, "", ""
