# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import sys
import os

sys.path.insert(0, os.path.abspath('..src'))
sys.path.insert(0, os.path.abspath('..src/exofop/download'))
sys.path.insert(0, os.path.abspath('..src/exofop/extract'))
sys.path.insert(0, os.path.abspath('..src/exofop/utils'))

language = "en"
master_doc = "index"

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'ExoFOP'
copyright = '2024, David Degen'
author = 'David Degen'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx_copybutton",
    "sphinx.ext.mathjax",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx_design",
    "myst_nb",
    "IPython.sphinxext.ipython_console_highlighting",
]


templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


source_suffix = {
    ".rst": "restructuredtext",
    ".ipynb": "myst-nb",
}

templates_path = ["_templates"]

myst_enable_extensions = ["dollarmath", "colon_fence"]


html_theme = "sphinx_book_theme"
html_title = "ExoFOP Documentation"
html_css_files = ["style.css"]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
html_static_path = ['_static']

html_theme_options = {
    "path_to_docs": "docs",
    "repository_url": "https://github.com/dgegen/exofop",
    "repository_branch": "main",
    "launch_buttons": {
        "binderhub_url": "https://mybinder.org",
        "notebook_interface": "jupyterlab",
        "colab_url": "https://colab.research.google.com/",
    },
    "use_edit_page_button": True,
    "use_issues_button": True,
    "use_repository_button": True,
    "use_download_button": True,
    "use_sidenotes": True,
}


nb_execution_mode = "off"
nb_execution_timeout = -1