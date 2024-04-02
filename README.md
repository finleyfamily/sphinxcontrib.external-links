# sphinxcontrib.external-links

Sphinx extension for easily adding reusable external links.

## Features

- default list of commonly used external links
- user configurable links
- check documentation for hardcoded links that can be replaced
- compatible with the Sphinx's `linkcheck` builder to check link integrity
- - global [substitutions](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#substitutions)

## Usage

```python
external_links = {
    "Google": "https://google.com",  # matches ":link:`google`", ":link:`Google`", etc
}
external_links_substitutions = {
    "dict": ":class:`dict`",
}
```

```rst
Provide a link to :link:`Google` to :link:`google.com <google>`.
This thing is a |dict|.
```
