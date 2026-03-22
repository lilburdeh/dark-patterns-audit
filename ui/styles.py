"""Custom CSS for the Dark Patterns Audit Tool.

Colour palette:
  Primary:   #0000FF (core blue)
  Secondary: #F7EFDE (stone), #FFFFFF (white), #000000 (black)
  Tertiary:  #97D9E3 (light blue), #18A48C (green), #9A1BBE (purple),
             #FDB633 (yellow), #A59BEE (lavender), #F6A4B7 (pink)

Font scale:
  Base:     1rem (16px)
  Small:    0.85rem (labels, tags)
  Body:     1rem
  Large:    1.1rem (emphasis)
  H3:       1.25rem
  H2:       1.6rem
  H1:       2.2rem
"""


def get_custom_css() -> str:
    """Return all custom CSS for the app."""
    return """
<style>
/* ===== GLOBAL ===== */
.block-container {
    padding-top: 4rem;
    padding-bottom: 2rem;
    font-size: 1rem;
}

/* Base font size for all Streamlit markdown */
.stMarkdown, .stMarkdown p {
    font-size: 1rem !important;
    line-height: 1.65 !important;
}

h1 {
    font-size: 2.2rem !important;
    font-weight: 700 !important;
    letter-spacing: -0.02em;
}

div h1[style*="color:#FFFFFF"], div h1[style*="color: #FFFFFF"] {
    color: #FFFFFF !important;
}

h2 {
    font-size: 1.6rem !important;
    font-weight: 600 !important;
    margin-top: 1.5rem !important;
    margin-bottom: 0.75rem !important;
}

h3 {
    font-size: 1.25rem !important;
    font-weight: 600 !important;
}

/* ===== SIDEBAR ===== */
section[data-testid="stSidebar"] {
    pointer-events: auto;
    resize: none;
    background-color: #F7EFDE;
    border-right: 1px solid #E8DFD0;
    min-width: 400px !important;
    max-width: 400px !important;
    width: 400px !important;
}

section[data-testid="stSidebar"] .stMarkdown,
section[data-testid="stSidebar"] .stMarkdown p {
    font-size: 1rem !important;
    line-height: 1.6 !important;
}

section[data-testid="stSidebar"] .stCaption p {
    font-size: 0.9rem !important;
}

section[data-testid="stSidebar"] > div:first-child {
    width: 400px !important;
}

/* Hide sidebar collapse button, resize handle, and close button */
[data-testid="collapsedControl"] { display: none !important; }
[data-testid="stSidebarResizeHandle"] { display: none !important; }
[data-testid="stSidebarCollapseButton"] { display: none !important; }
button[kind="headerNoPadding"] { display: none !important; }

/* ===== METRIC CARDS ===== */
.metric-card {
    background: white;
    border: 1px solid #E8DFD0;
    border-radius: 10px;
    padding: 1.2rem 1rem;
    text-align: center;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);
    border-top: 4px solid #000000;
    position: relative;
    cursor: default;
}

/* ===== METRIC CARD TOOLTIPS ===== */
.metric-card[data-tooltip]::after {
    content: attr(data-tooltip);
    position: absolute;
    inset: 0;
    background: rgba(235, 235, 235, 0.93);
    color: #111111;
    padding: 0.9rem 0.85rem;
    border-radius: 10px;
    font-size: 0.8rem;
    font-weight: 400;
    line-height: 1.5;
    text-align: center;
    display: flex;
    align-items: center;
    justify-content: center;
    pointer-events: none;
    opacity: 0;
    transition: opacity 0.15s ease;
    z-index: 9999;
    backdrop-filter: blur(2px);
}

.metric-card[data-tooltip]:hover::after {
    opacity: 1;
}

.metric-card.high { border-top-color: #F6A4B7; }
.metric-card.medium { border-top-color: #FDB633; }
.metric-card.low { border-top-color: #18A48C; }
.metric-card.total { border-top-color: #0000FF; }

.metric-card .metric-value {
    font-size: 2.2rem;
    font-weight: 700;
    line-height: 1.2;
    margin-bottom: 0.25rem;
    color: #000000;
}

.metric-card .metric-label {
    font-size: 0.85rem;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: #000000;
    font-weight: 600;
    opacity: 0.6;
}

/* ===== RISK BANNER ===== */
.risk-banner {
    padding: 0.85rem 1.5rem;
    border-radius: 8px;
    font-weight: 700;
    font-size: 1.1rem;
    text-align: center;
    margin-bottom: 1rem;
    color: white;
}

.risk-banner.high { background-color: #F6A4B7; color: #000000; }
.risk-banner.medium { background-color: #FDB633; color: #000000; }
.risk-banner.low { background-color: #18A48C; }
.risk-banner.clean { background-color: #000000; }

/* ===== SEVERITY BADGES ===== */
.severity-badge {
    display: inline-block;
    padding: 4px 14px;
    border-radius: 99px;
    font-size: 0.85rem;
    font-weight: 700;
    color: white;
    letter-spacing: 0.02em;
}

.severity-badge.high { background-color: #F6A4B7; color: #000000; }
.severity-badge.medium { background-color: #FDB633; color: #000000; }
.severity-badge.low { background-color: #18A48C; }

/* ===== FINDING EXPANDERS ===== */
div[data-testid="stExpander"] {
    border: 1px solid #E8DFD0 !important;
    border-radius: 8px !important;
    margin-bottom: 0.75rem !important;
    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.04);
}

div[data-testid="stExpander"] details summary {
    font-weight: 600 !important;
    font-size: 1rem !important;
}

div[data-testid="stExpander"] details summary span {
    font-size: 1rem !important;
}

/* ===== FINDINGS TABLE ===== */
.stDataFrame {
    border-radius: 8px;
    overflow: hidden;
    font-size: 0.95rem;
}

/* ===== BUTTONS ===== */
.stButton > button[kind="primary"] {
    font-size: 1.05rem;
    font-weight: 600;
    padding: 0.7rem 1.5rem;
    border-radius: 8px;
    background-color: #0000FF;
}

.stButton > button[kind="secondary"] {
    font-size: 1rem;
    border-radius: 8px;
}

.stButton > button[kind="secondary"]:hover {
    background-color: #000000 !important;
    color: white !important;
    border-color: #000000 !important;
}

/* Browse files button hover */
[data-testid="stFileUploaderDropzone"] button:hover {
    background-color: #000000 !important;
    color: white !important;
    border-color: #000000 !important;
}

[data-testid="stFileUploaderDropzone"] button:hover span {
    color: white !important;
}

/* File uploader text */
[data-testid="stFileUploaderDropzone"] {
    font-size: 1rem;
}

/* ===== DOWNLOAD BUTTONS ===== */
.stDownloadButton > button {
    border-radius: 8px;
    font-weight: 600;
    font-size: 1rem;
}

/* ===== SECTION DIVIDER ===== */
hr {
    margin-top: 1.5rem !important;
    margin-bottom: 1.5rem !important;
    border-color: #E8DFD0 !important;
}

/* ===== FINDING DETAIL SECTIONS ===== */
.finding-section {
    padding: 0.5rem 0;
    border-bottom: 1px solid #F7EFDE;
    margin-bottom: 0.5rem;
}

.finding-section:last-child {
    border-bottom: none;
}

.finding-section-label {
    font-size: 0.85rem;
    text-transform: uppercase;
    letter-spacing: 0.04em;
    color: #000000;
    font-weight: 600;
    margin-bottom: 0.25rem;
    opacity: 0.5;
}

/* ===== REGULATORY TAG ===== */
.reg-tag {
    display: inline-block;
    background: #F7EFDE;
    color: #0000FF;
    border: 1px solid #0000FF;
    border-radius: 6px;
    padding: 3px 10px;
    font-size: 0.85rem;
    font-weight: 600;
    margin-right: 4px;
    margin-bottom: 4px;
}

/* ===== TEXT INPUT ===== */
/* Target the BaseWeb container — this is the visible box with the border */
.stTextInput [data-baseweb="input"] {
    min-height: 55px !important;
    align-items: flex-start !important;
    padding-top: 0.85rem !important;
    padding-bottom: 0.85rem !important;
}

/* Raw input element — horizontal padding only, anchored to top of container */
.stTextInput input {
    font-size: 1rem !important;
    padding: 0 1.25rem !important;
    align-self: flex-start !important;
    margin-top: 0 !important;
}
</style>
"""
