"""Pytest configuration, fixtures, and plugins."""

from __future__ import annotations

import re
from pathlib import Path

import pytest

TEST_ROOT = Path(__file__).parent

ANSI_ESCAPE_PATTERN = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")
"""Pattern to match ANSI escape sequences."""


@pytest.fixture(scope="session")
def fixture_dir() -> Path:
    """Path to the fixture directory."""
    return Path(__file__).parent / "fixtures"


@pytest.fixture(scope="session")
def rootdir(fixture_dir: Path) -> Path:
    """Provide a ``rootdir`` for Sphinx fixtures."""
    return fixture_dir


# @pytest.fixture()
# def warning(app: SphinxTestApp) -> list[str]:
#     """Override ``sphinx.testing.fixtures.warning``."""
#     txt = app._warning.getvalue()  # TODO (kyle): change to app.warning after next sphinx release
#     return [ANSI_ESCAPE_PATTERN.sub("", i) for i in txt.split("\n")]
