"""Test sphinxcontrib.external_links._transforms."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from ..utils import strip_ansi

if TYPE_CHECKING:
    from io import StringIO

    from sphinx.testing.util import SphinxTestApp


@pytest.mark.sphinx(
    "html",
    testroot="hardcoded-urls",
    confoverrides={"external_links_detect_hardcoded_links": False},
)
def test_hardcoded_urls(app: SphinxTestApp, warning: StringIO) -> None:
    """Test ExternalLinkChecker no warnings."""
    app.build()
    assert not warning.getvalue()


@pytest.mark.sphinx("html", testroot="hardcoded-urls")
def test_hardcoded_urls_emit_warnings(app: SphinxTestApp, warning: StringIO) -> None:
    """Test ExternalLinkChecker emit warnings."""
    app.build()
    warning_output = strip_ansi(warning.getvalue())

    # there should be exactly three warnings for replaceable URLs
    message = (
        'index.rst:{line_num}: WARNING: hardcoded link "{title}" to {target} '
        "could be replaced by a reference ({reference})"
    )
    assert (
        message.format(
            line_num=16,
            title="https://google.com",
            target="https://google.com",
            reference=":link:`https://google.com <google>`",
        )
        in warning_output
    )
    assert (
        message.format(
            line_num=17,
            title="google",
            target="https://google.com",
            reference=":link:`google`",
        )
        in warning_output
    )
    assert (
        message.format(
            line_num=19,
            title="replaceable link",
            target="https://github.com",
            reference=":link:`replaceable link <github>`",
        )
        in warning_output
    )
    assert (
        message.format(
            line_num=20,
            title="inline replaceable link",
            target="https://github.com/",
            reference=":link:`inline replaceable link <github>`",
        )
        in warning_output
    )
