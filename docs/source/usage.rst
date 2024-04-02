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

2. *(optional)* Add your own mapping of external links using :data:`external_links`.

   .. code-block:: python
    :caption: conf.py
    :linenos:

    external_links = {
        "Google": "https://google.com",  # matches ":link:`google`", ":link:`Google`", etc
    }

3. Use the ``:link:`` role in your documentation to use the external link.

   .. tab-set::

    .. tab-item:: Source (rst)

      .. code-block:: rst

        Provide a link to :link:`Google` to :link:`google.com <google>`.

    .. tab-item:: Output

      Provide a link to :link:`Google` to :link:`google.com <google>`.
