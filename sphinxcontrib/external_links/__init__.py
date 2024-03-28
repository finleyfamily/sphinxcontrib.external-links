"""Sphinx extension sphinxcontrib.external-links."""

from __future__ import annotations

from importlib.metadata import PackageNotFoundError, version
from typing import TYPE_CHECKING

from . import constants, type_defs
from ._roles import links_role

if TYPE_CHECKING:
    from sphinx.application import Sphinx

try:
    __version__ = version(__name__)
except PackageNotFoundError:  # cov: ignore
    # package is not installed
    __version__ = "0.0.0"


def setup_roles(app: Sphinx) -> None:
    """Setup roles."""
    app.add_role("link", links_role(app.config.external_links))


def setup(app: Sphinx) -> type_defs.ExtensionMetadata:
    """Setup extension."""
    app.add_config_value("external_links", default={}, rebuild="env")
    app.add_config_value("external_links_detect_hardcoded_links", default=True, rebuild="env")
    app.connect("builder-inited", setup_roles)
    return {"version": __version__, "parallel_read_safe": True}


__all__ = ["constants", "type_defs"]
