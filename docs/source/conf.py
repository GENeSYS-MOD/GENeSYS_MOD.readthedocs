# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'GENeSYS-MOD | The Global Energy System Model'
copyright = '2025, the GENeSYS-MOD community'
author = 'The GENeSYS-MOD Community'

release = '0.3'
version = 'V 0.3.1'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.bibtex',
    'myst_parser',
    "sphinx_github_changelog",
]

# Provide a GitHub API token:
# Pass the SPHINX_GITHUB_CHANGELOG_TOKEN environment variable to your build
# OR
# You can retrieve your token any other way you want, but of course, please
# don't commit secrets to git, especially on a public repository
#sphinx_github_changelog_token = 123456

bibtex_bibfiles = ['references.bib']
bibtex_default_style = 'plain'

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_logo = '_static/logo.png'
html_css_files = ["custom.css"]

html_theme_options = {
    #'analytics_id': 'G-XXXXXXXXXX',  #  Provided by Google in your dashboard
    #'analytics_anonymize_ip': False,
    'logo_only': True,
    'prev_next_buttons_location': 'None',
    'style_external_links': False,
    #'vcs_pageview_mode': '',
    #'style_nav_header_background': 'white',
    #'flyout_display': 'hidden',
    'version_selector': True,
    'language_selector': False,
    # Toc options
    #'collapse_navigation': True,
    #'sticky_navigation': True,
    #'navigation_depth': 4,
    #'includehidden': True,
    #'titles_only': False
}

# -- Options for EPUB output
epub_show_urls = 'footnote'