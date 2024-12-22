# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'RedSun'
copyright = '2024, Jacopo Abramo'
author = 'Jacopo Abramo'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    "sphinx.ext.githubpages",
    "sphinxcontrib.bibtex",
    'myst_parser',
]

templates_path = ['_templates']
exclude_patterns = ['_build', "README.md"]

source_suffix = 'md'

bibtex_bibfiles = ["statement.bib"]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

napoleon_numpy_docstring = True
autodoc_typehints = 'description'
