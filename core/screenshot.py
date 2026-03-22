"""URL to screenshot capture and HTML source fetching using Playwright."""

from __future__ import annotations


def is_playwright_available() -> bool:
    """Check if Playwright is installed and usable."""
    try:
        from playwright.sync_api import sync_playwright
        return True
    except ImportError:
        return False


def capture_url(url: str) -> tuple[bytes | None, str | None]:
    """Capture a full-page screenshot and HTML source of a URL in one browser session.

    Args:
        url: The URL to capture.

    Returns:
        Tuple of (screenshot_bytes, html_source). Either may be None on failure.
    """
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        return None, None

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page(viewport={"width": 1280, "height": 900})
            page.goto(url, timeout=30000, wait_until="networkidle")
            screenshot_bytes = page.screenshot(full_page=True, type="png")
            html_source = page.content()
            browser.close()
            return screenshot_bytes, html_source
    except Exception:
        return None, None


def capture_screenshot(url: str) -> bytes | None:
    """Backwards-compatible wrapper — returns screenshot only."""
    screenshot, _ = capture_url(url)
    return screenshot
