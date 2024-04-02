#####
Usage
#####

1. Install and enable this extension.

   .. code-block:: python
    :caption: conf.py
    :linenos:

    extensions = [
        "sphinxcontrib.external_links",
    ]

2. *(optional)* Add your own mapping of external links using :data:`external_links` and :link:`substitutions` using :data:`external_links_substitutions`.

   .. code-block:: python
    :caption: conf.py
    :linenos:

    external_links = {
        "Google": "https://google.com",  # matches ":link:`google`", ":link:`Google`", etc
    }
    external_links_substitutions = {
        "dict": ":class:`dict`"
    }

3. Use the ``:link:`` role in your documentation to use the external link.

   .. tab-set::

    .. tab-item:: Source (rst)

      .. code-block:: rst

        Provide a link to :link:`Google` to :link:`google.com <google>`.
        Describe something as a |dict|.

    .. tab-item:: Output

      Provide a link to :link:`Google` to :link:`google.com <google>`.
      Describe something as a :class:`dict`.
