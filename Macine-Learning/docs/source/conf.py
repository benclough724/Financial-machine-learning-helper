# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Financial inidication - Machine learning project'
copyright = '2025, Ben Clough'
author = 'Ben Clough'
release = '2024'

import os
import sys
sys.path.insert(0, os.path.abspath('../../../'))

# auto build the comments for testing purposes 
# sphinx-autobuild source build/html


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    # GPT generated extensions to save time
    # OpenAI, 2025. ChatGPT [online]. (July 5 version). Available at: https://chat.openai.com/ [Accessed 4 July 2025].
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',  # For Google/NumPy style docstrings
    'sphinx.ext.viewcode',  # Adds links to source code
    ]

html_theme = 'alabaster'  # Theme for HTML documentation

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
