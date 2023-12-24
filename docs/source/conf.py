# Copyright © 2023 SafeLlama.

# -*- coding: utf-8 -*-

import os
import subprocess

# -- Project information -----------------------------------------------------

project = "Plexiglass"
copyright = "2023, SafeLlama"
author = "SafeLlama"
version = "0.0.1"
release = "0.0.1"

# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
]

python_use_unqualified_type_names = True
autosummary_generate = True

intersphinx_mapping = {
    "https://docs.python.org/3": None,
    "https://numpy.org/doc/stable/": None,
}

templates_path = ["_templates"]
html_static_path = ["_static"]
source_suffix = ".rst"
master_doc = "index"
highlight_language = "python"
pygments_style = "sphinx"

# -- Options for HTML output -------------------------------------------------

html_theme = "sphinx_book_theme"

html_theme_options = {
    "show_toc_level": 2,
    "repository_url": "https://github.com/safellama/plexiglass",
    "use_repository_button": True,
    "navigation_with_keys": False,
}

html_logo = "_static/plexiglass.png"

html_title = "Plexiglass"


# -- Options for HTMLHelp output ---------------------------------------------

htmlhelp_basename = "plexiglass_doc"