#############
Configuration
#############

This extension contributes two configuration fields to ``conf.py``.

.. data:: external_links
  :type: Mapping[str, str]
  :value: {}

  Mapping of case-insensitive external links and the target used to reference them.

  .. code-block:: python
    :linenos:

    external_links = {
        "Google": "https://google.com",  # matches ":link:`google`", ":link:`Google`", etc
    }

.. data:: external_links_detect_hardcoded_links
  :type: bool
  :value: True

  Emit a warning when a hardcoded link can be replaced using the ``:link:`` role.


.. data:: external_links_substitutions
  :type: Mapping[str, str]
  :value: {}

  Mapping of :link:`substitutions`.

  :link:`Substitutions` are processed after default :link:`substitutions` like ``|release|``, ``|version|`` and ``|today|``, but before any others in source files.

  .. code-block:: python
    :linenos:

    external_links_substitutions = {
        "dict": ":class:`dict`"
    }
