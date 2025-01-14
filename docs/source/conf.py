"""Sphinx config file.

https://www.sphinx-doc.org/en/master/usage/configuration.html

"""

from __future__ import annotations

import os
from datetime import date
from pathlib import Path

import tomllib

from sphinxcontrib.external_links import __version__

DOCS_DIR = Path(__file__).parent.parent.resolve()
ROOT_DIR = DOCS_DIR.parent
SRC_DIR = DOCS_DIR / "source"

PYPROJECT_TOML = tomllib.loads((ROOT_DIR / "pyproject.toml").read_text())
"""Read in the contents of ``../../pyproject.toml`` to reuse it's values."""


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
project = PYPROJECT_TOML["project"]["name"]
copyright = f"{date.today().year}, Kyle Finley"  # noqa: A001, DTZ011
author = PYPROJECT_TOML["project"]["authors"][0]["name"]
release = __version__
version = ".".join(release.split(".")[:2])  # short X.Y version


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
add_function_parentheses = True
add_module_names = False
default_role = None
exclude_patterns = []
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosectionlabel",  # creates references for each section that can be linked back to
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinxcontrib.external_links",
    "sphinxcontrib.jquery",
    "sphinxcontrib_trio",
]
highlight_language = "default"
language = "en"
master_doc = "index"
primary_domain = "py"
pygments_style = "one-dark"  # syntax highlighting style
pygments_dark_style = "one-dark"  # syntax highlighting style
source_suffix = {".rst": "restructuredtext"}
templates_path = ["_templates"]  # template dir relative to this dir


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_codeblock_linenos_style = "inline"
html_css_files = [
    "css/custom.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/fontawesome.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/solid.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/brands.min.css",
]  # files relative to html_static_path
html_js_files = ["js/custom.js"]
html_theme = "furo"  # theme to use for HTML and HTML Help pages
html_theme_options: dict[str, bool | dict[str, str] | list[str] | str] = {
    "dark_css_variables": {
        "font-stack--monospace": "Inconsolata, monospace",
        "color-inline-code-background": "#24242d",
    },
    "light_css_variables": {
        "font-stack--monospace": "Inconsolata, monospace",
    },
    "top_of_page_buttons": [],
}
html_title = f"{project} v{version}"
html_show_copyright = True
html_show_sphinx = False
html_static_path = ["_static"]  # dir with static files relative to this dir


# -- Options for sphinx-apidoc -----------------------------------------------
# https://www.sphinx-doc.org/en/master/man/sphinx-apidoc.html#environment
os.environ["SPHINX_APIDOC_OPTIONS"] = "members"


# -- Options for sphinx_copybutton ---------------------------------
# https://sphinx-copybutton.readthedocs.io/en/latest/index.html
copybutton_prompt_text = r">>> |\.\.\. |\$ |In \[\d*\]: | {2,5}\.\.\.: | {5,8}: "
copybutton_prompt_is_regexp = True
copybutton_remove_prompts = True
copybutton_line_continuation_character = "\\"


# -- Options of sphinx.ext.autodoc -------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#configuration
autoclass_content = "class"
autodoc_class_signature = "separated"
autodoc_default_options = {
    "member-order": "alphabetical",
    "members": True,
    "show-inheritance": True,
}
autodoc_inherit_docstrings = True
autodoc_member_order = "alphabetical"
autodoc_type_aliases = {}
autodoc_typehints = "signature"
autodoc_typehints_format = "short"


# -- Options of sphinx.ext.intersphinx ------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),  # link to python docs
}


# -- Options of sphinx.ext.autosectionlabel ----------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/autosectionlabel.html
autosectionlabel_maxdepth = 2
autosectionlabel_prefix_document = True


# -- Options for sphinx.ext.napoleon  ----------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html#configuration
napoleon_attr_annotations = True
napoleon_google_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_type_aliases = autodoc_type_aliases
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True


# -- Options for sphinx.ext.todo ---------------------------------------------
# https://www.sphinx-doc.org/page/usage/extensions/todo.html
todo_include_todos = True


# -- Options for sphinxcontrib.external_links  --------------------------------
external_links = {
    "substitutions": "https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#substitutions",
}
