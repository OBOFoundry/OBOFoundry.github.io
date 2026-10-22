"""Tests for shared website templates."""

import unittest
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


class IconParser(HTMLParser):
    """Collect favicon links from HTML."""

    def __init__(self):
        """Initialize the parser."""
        super().__init__()
        self.icons = []

    def handle_starttag(self, tag, attrs):
        """Record links whose relation includes icon."""
        attrs = dict(attrs)
        if tag == "link" and "icon" in (attrs.get("rel") or "").split():
            self.icons.append(attrs)


class TestSite(unittest.TestCase):
    """Test the shared website head."""

    def test_favicon(self):
        """Test that the favicon uses the existing blacksmith PNG."""
        parser = IconParser()
        parser.feed(ROOT.joinpath("_includes", "head.html").read_text())
        self.assertEqual(1, len(parser.icons), msg="Missing shared favicon link")
        icon = parser.icons[0]
        self.assertEqual("image/png", icon.get("type"))
        self.assertEqual("/images/foundrylogo.png", icon.get("href"))
        image = ROOT.joinpath(icon["href"].lstrip("/"))
        self.assertEqual(b"\x89PNG\r\n\x1a\n", image.read_bytes()[:8])

    def test_default_layout_includes_head(self):
        """Test that pages using the default layout get the shared head."""
        layout = ROOT.joinpath("_layouts", "default.html").read_text()
        self.assertRegex(layout, r"{%-?\s*include\s+head\.html\s*-?%}")
