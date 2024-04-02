"""Constants."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Mapping


COMMON_LINKS: Mapping[str, str] = {
    "Google": "https://google.com",
}
"""Mapping of common links."""
