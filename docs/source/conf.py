# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'plexiglass'
copyright = '2023, kortex-labs'
author = 'kortex-labs'

# The full version, including alpha/beta/rc tags
release = '0.0.1'


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
    "repository_url": "https://github.com/kortex-labs/plexiglass",
    "use_repository_button": True,
    "navigation_with_keys": False,
}


# -- Options for HTMLHelp output ---------------------------------------------

htmlhelp_basename = "mlx_doc"