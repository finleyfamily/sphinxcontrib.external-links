"""Test sphinxcontrib.external_links._roles."""

from __future__ import annotations

from typing import TYPE_CHECKING
from unittest.mock import Mock

from sphinxcontrib.external_links._case_insensitive_mapping import CaseInsensitiveMapping
from sphinxcontrib.external_links._roles import links_role
from sphinxcontrib.external_links.constants import COMMON_LINKS

if TYPE_CHECKING:
    from pytest_mock import MockerFixture

MODULE = "sphinxcontrib.external_links._roles"


def test_links_role(mocker: MockerFixture) -> None:
    """Test links_role."""
    find_uri = mocker.patch(f"{MODULE}._find_uri", return_value="find_uri")
    links = CaseInsensitiveMapping(COMMON_LINKS)
    mapping_kls = mocker.patch(f"{MODULE}.CaseInsensitiveMapping", return_value=links)
    reference = mocker.patch(f"{MODULE}.reference", return_value="reference")
    split_explicit_title = mocker.patch(
        f"{MODULE}.split_explicit_title", return_value=("has_explicit", "title", "Target")
    )
    unescape = mocker.patch(f"{MODULE}.unescape", return_value="unescaped")

    role_func = links_role()
    mapping_kls.assert_called_once_with(COMMON_LINKS)
    assert role_func("role", "rawtext", "text", 0, Mock(), {}, []) == (
        [reference.return_value],
        [],
    )
    unescape.assert_called_once_with("text")
    split_explicit_title.assert_called_once_with(unescape.return_value)
    find_uri.assert_called_once_with(links, "target")
    reference.assert_called_once_with("title", "title", internal=False, refuri=find_uri.return_value)


def test_links_role_user_links(mocker: MockerFixture) -> None:
    """Test links_role."""
    links = CaseInsensitiveMapping(COMMON_LINKS, test="foo.bar")
    mapping_kls = mocker.patch(f"{MODULE}.CaseInsensitiveMapping", return_value=links)
    reference = mocker.patch(f"{MODULE}.reference", return_value="reference")

    role_func = links_role({"test": "foo.bar"})
    mapping_kls.assert_called_once_with(COMMON_LINKS, test="foo.bar")
    assert role_func("role", "rawtext", "test", 0, Mock(), {}, []) == (
        [reference.return_value],
        [],
    )
    reference.assert_called_once_with("test", "test", internal=False, refuri="foo.bar")
