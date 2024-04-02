"""Test utilities."""

from __future__ import annotations

import re

ANSI_ESCAPE_PATTERN = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")
"""Pattern to match ANSI escape sequences."""


def strip_ansi(value: str) -> str:
    """Strip ANSI escape sequences."""
    return ANSI_ESCAPE_PATTERN.sub("", value)
