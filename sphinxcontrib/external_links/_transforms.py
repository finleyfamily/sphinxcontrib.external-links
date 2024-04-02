"""External link checker."""

from __future__ import annotations

import re

from docutils.nodes import reference
from sphinx.transforms.post_transforms import SphinxPostTransform
from sphinx.util import logging

from ._case_insensitive_mapping import CaseInsensitiveMapping
from .constants import COMMON_LINKS

LOGGER = logging.getLogger(__name__)


class ExternalLinkChecker(SphinxPostTransform):
    """Check each external link to see if it can be replaced with a reference."""

    _external_links: CaseInsensitiveMapping
    default_priority = 501

    def run(self, **_kwargs: object) -> None:
        """Main method of post transforms."""
        if not self.config.external_links_detect_hardcoded_links:
            return

        self._external_links = CaseInsensitiveMapping(
            COMMON_LINKS, **self.app.config.external_links
        )
        for refnode in self.document.findall(reference):
            self.check_reference(refnode)

    def check_reference(self, ref_node: reference) -> None:
        """Check if the reference can be replaced.

        Args:
            links: Mapping of referencable links.
            ref_node: The reference node to check.

        """
        if "internal" in ref_node or "refuri" not in ref_node:
            return

        matches = self._external_links.find_value(
            re.compile(re.escape(ref_node["refuri"]) + r"?(/)$")
        )
        if not matches:
            return

        LOGGER.warning(
            'hardcoded link "%s" to %s could be replaced by a reference (%s)',
            ref_node.astext(),
            ref_node["refuri"],
            ", ".join(self.make_suggestions(matches, ref_node)),
            location=ref_node,
        )

    def make_suggestions(self, matches: CaseInsensitiveMapping, ref_node: reference) -> list[str]:
        """Make suggestions based on matches."""
        title = ref_node.astext()
        rv: list[str] = []
        for k in matches:
            if not ref_node["refuri"].startswith(title) and title == k:
                rv.append(f":link:`{k}`")
            else:
                rv.append(f":link:`{title} <{k}>`")
        return rv
