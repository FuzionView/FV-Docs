# Configuration file for the Sphinx documentation builder.

project = 'FuzionView'
copyright = '2025 SharedGeo CC-BY-SA-4.0 test'
author = 'SharedGeo'
release = '1.0'

extensions = [
	'sphinx.ext.autosectionlabel',
	'sphinxcontrib.video',
]

html_show_sourcelink = False

templates_path = ['_templates']
exclude_patterns = []

#html_theme_options = {
#    `display_version` : True,
#    `prev_next_buttons_location` : Both,
#}

html_theme_options = {
    'collapse_navigation': True
}

html_favicon = "_static/fuzionviewicon.ico"

import sphinx_rtd_theme
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_css_files = ['css/custom.css']
html_js_files = ['js/custom.js']
