# Configuration file for the Sphinx documentation builder.
#import os
import sys
import os
sys.path.insert(0, os.path.abspath('C:/Users/User/OneDrive/Ambiente de Trabalho/ADC-TP2-TM/ADC-TP2-TM'))

# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'ADC-TP2-TM'
copyright = '2025, MARTIM TIAGO'
author = 'MARTIM TIAGO'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',  # corrigido
    'sphinx.ext.napoleon'  # se usas docstrings no estilo Google/NumPy
]


templates_path = ['_templates']
exclude_patterns = []
autodoc_mock_imports = ["db", "utils"]
autodoc_mock_imports = ["logs", "db"]
autodoc_mock_imports = ["utils"]




# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_logo = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTgPYZRra1NzQLKONj0okNXk723x5hbRkMmCA&s'         # Coloca um logo na pasta docs/_static/
html_favicon = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTgPYZRra1NzQLKONj0okNXk723x5hbRkMmCA&s'   # Ícone da aba do navegador
html_theme_options = {
    'navigation_depth': 4,
    'collapse_navigation': False,
    'sticky_navigation': True
}

