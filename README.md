# sphinxcontrib.external-links

Sphinx extension for easily adding reusable external links.

## Features

- default list of commonly used external links
- user configurable links
- check documentation for hardcoded links that can be replaced
- compatible with the Sphinx's `linkcheck` builder to check link integrity

## Usage

```python
external_links = {
    "Google": "https://google.com",  # matches ":link:`google`", ":link:`Google`", etc
}
```

```rst
Provide a link to :link:`Google` to :link:`google.com <google>`.
```
