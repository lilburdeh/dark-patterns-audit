"""Reusable UI components for the Dark Patterns Audit Tool."""

import plotly.graph_objects as go

from config.settings import SEVERITY_COLORS


def severity_badge(level: str) -> str:
    """Return an HTML badge for a severity level."""
    css_class = level.lower()
    return f'<span class="severity-badge {css_class}">{level}</span>'


def risk_banner(level: str) -> str:
    """Return a full-width risk level banner."""
    css_class = level.lower()
    return f'<div class="risk-banner {css_class}">Overall Risk: {level}</div>'


def metric_card(value: int, label: str, card_class: str = "", tooltip: str = "") -> str:
    """Return an HTML metric card with optional hover tooltip."""
    tooltip_attr = f' data-tooltip="{tooltip}"' if tooltip else ""
    return (
        f'<div class="metric-card {card_class}"{tooltip_attr}>'
        f'<div class="metric-value">{value}</div>'
        f'<div class="metric-label">{label}</div>'
        f'</div>'
    )


def regulatory_tag(ref: str) -> str:
    """Return a styled regulatory reference tag."""
    return f'<span class="reg-tag">{ref}</span>'


def severity_chart(summary: dict) -> go.Figure:
    """Create a horizontal bar chart of severity distribution."""
    categories = ["High", "Medium", "Low"]
    values = [summary.get("high", 0), summary.get("medium", 0), summary.get("low", 0)]
    colors = [SEVERITY_COLORS["High"], SEVERITY_COLORS["Medium"], SEVERITY_COLORS["Low"]]

    fig = go.Figure(
        go.Bar(
            x=values,
            y=categories,
            orientation="h",
            marker_color=colors,
            text=values,
            textposition="inside",
            textfont=dict(size=14, color="white", family="Arial"),
        )
    )
    total = max(sum(values), 1)
    fig.update_layout(
        height=160,
        margin=dict(l=0, r=20, t=5, b=5),
        xaxis=dict(showticklabels=False, showgrid=False, zeroline=False, range=[0, total * 3]),
        yaxis=dict(autorange="reversed", tickfont=dict(size=13, family="Arial")),
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        bargap=0.35,
    )
    return fig
