import sys, os, subprocess
from recommonmark.parser import CommonMarkParser
app_path = os.path.abspath('../sample')
sys.path.insert(0, app_path)
print sys.path
try:
    version_git = subprocess.check_output(["git", "describe", "--tags"]).rstrip()
except:
    version_git = '0.0.0'
extensions = []
source_parsers = {
    '.md': CommonMarkParser,
}
templates_path = ['_templates']
source_suffix = ['.rst', '.md']
master_doc = 'index'
project = u'sample'
copyright = u'2012, Fred Vassard'
version = version_git
release = version_git
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
