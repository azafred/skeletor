import sys, os
from recommonmark.parser import CommonMarkParser
app_path = os.path.abspath('../sample')
print app_path
sys.path.insert(0, app_path)
print sys.path

extensions = []
source_parsers = {
    '.md': CommonMarkParser,
}
templates_path = ['_templates']
source_suffix = ['.rst', '.md']
master_doc = 'index'
project = u'sample'
copyright = u'2012, Fred Vassard'
version = 'v0.0.1'
release = 'v0.0.1'
exclude_patterns = ['_build']
pygments_style = 'pastie'
html_theme = 'agogo'
htmlhelp_basename = 'sampledoc'
latex_elements = {
}
latex_documents = [
  ('index', 'sample.tex', u'sample Documentation',
   u'Fred Vassard', 'manual'),
]
man_pages = [
    ('index', 'sample', u'sample Documentation',
     [u'Fred Vassard'], 1)
]
texinfo_documents = [
  ('index', 'sample', u'sample Documentation',
   u'Fred Vassard', 'sample', 'One line description of project.',
   'Miscellaneous'),
]
