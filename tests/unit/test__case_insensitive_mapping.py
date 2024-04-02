"""Test sphinxcontrib.external_links._case_insensitive_mapping."""

from __future__ import annotations

import re
from typing import TYPE_CHECKING

import pytest

from sphinxcontrib.external_links._case_insensitive_mapping import CaseInsensitiveMapping

if TYPE_CHECKING:
    from collections.abc import Mapping

    from pytest_mock import MockerFixture

MODULE = "sphinxcontrib.external_links._case_insensitive_mapping"


class TestCaseInsensitiveMapping:
    """Test CaseInsensitiveMapping."""

    @pytest.mark.parametrize(
        ("data", "kwargs", "expected"),
        [
            ({"key0": "data", "KeY1": "data"}, {}, {"key0": "data", "key1": "data"}),
            (
                {"key0": "data", "KeY1": "data"},
                {"KeY1": "kwargs"},
                {"key0": "data", "key1": "kwargs"},
            ),
            (
                {"key0": "data", "KeY1": "data"},
                {"key0": "kwargs"},
                {"key0": "kwargs", "key1": "data"},
            ),
            ({}, {"key0": "data", "KeY1": "kwargs"}, {"key0": "data", "key1": "kwargs"}),
        ],
    )
    def test___init__(
        self, data: Mapping[str, str], expected: Mapping[str, str], kwargs: Mapping[str, str]
    ) -> None:
        """Test __init__."""
        result = CaseInsensitiveMapping(data, **kwargs)
        assert result._store == expected

    @pytest.mark.parametrize("key", ["key", "KeY"])
    def test___getitem__(self, key: str) -> None:
        """Test __getitem__."""
        assert CaseInsensitiveMapping({"key": "val"})[key] == "val"

    def test___hash__(self, mocker: MockerFixture) -> None:
        """Test __hash__."""
        mock_frozenset = mocker.patch(f"{MODULE}.frozenset", return_value="frozenset")
        mock_hash = mocker.patch(f"{MODULE}.hash", return_value=9001)
        items = mocker.patch.object(
            CaseInsensitiveMapping, "items", return_value=iter({"key": "val"})
        )
        assert hash(CaseInsensitiveMapping(key="val")) == mock_hash.return_value
        mock_frozenset.assert_called_once_with(items.return_value)
        mock_hash.assert_called_once_with(mock_frozenset.return_value)

    def test___iter__(self, mocker: MockerFixture) -> None:
        """Test __iter__."""
        mock_iter = mocker.patch(f"{MODULE}.iter", return_value=iter({"key": "val"}))
        obj = CaseInsensitiveMapping(key="val")
        assert list(iter(obj)) == ["key"]
        mock_iter.assert_called_once_with(obj._store)

    def test___len__(self, mocker: MockerFixture) -> None:
        """Test __len__."""
        mock_len = mocker.patch(f"{MODULE}.len", return_value=3)
        obj = CaseInsensitiveMapping(key="val")
        assert len(obj) == mock_len.return_value
        mock_len.assert_called_once_with(obj._store)

    @pytest.mark.parametrize(
        ("pattern", "expected"),
        [
            ("foo.bar-val", {"foo.bar": "foo.bar-val"}),
            (r"bar\..+", {}),
            (re.compile(r"bar\..+"), {"bar.foo": "bar.foo-val"}),
            (re.compile(r"bar.*"), {"bar": "bar-val", "bar.foo": "bar.foo-val"}),
        ],
    )
    def test_find_value(self, expected: dict[str, str], pattern: re.Pattern[str] | str) -> None:
        """Test find_value."""
        assert (
            CaseInsensitiveMapping(
                {i: f"{i}-val" for i in ("foo", "foo.bar", "foo.baz", "bar", "bar.foo")}
            )
            .find_value(pattern)
            ._store
            == expected
        )
