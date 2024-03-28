"""case-insensitive :class:`collections.abc.Mapping`."""

from __future__ import annotations

from collections import OrderedDict
from collections.abc import Mapping
from typing import TYPE_CHECKING, TypeVar

if TYPE_CHECKING:
    from collections.abc import Generator

_V = TypeVar("_V")


class CaseInsensitiveMapping(Mapping[str, _V]):
    """A case-insensitive :class:`collections.abc.Mapping` object."""

    def __init__(self, data: Mapping[str, _V] | None = None, **kwargs: _V) -> None:
        """Instantiate class."""
        data = {} if data is None else {k.lower(): v for k, v in data.items()}
        self._store = OrderedDict(data)
        self._store.update(**{k.lower(): v for k, v in kwargs.items()})

    def __getitem__(self, key: str) -> _V:
        """Get value from object, ignoring case."""
        return self._store[key.lower()]

    def __hash__(self) -> int:
        """Make the object hashable."""
        return hash(frozenset(self.items()))

    def __iter__(self) -> Generator[str, _V, None]:
        """Iterate over object."""
        yield from iter(self._store)

    def __len__(self) -> int:
        """Length of object."""
        return len(self._store)
