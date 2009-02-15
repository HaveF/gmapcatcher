from distutils.core import setup
import py2exe

setup(
    name = 'gmapcatcher',
    description = 'Offline Google Map Viewer',
    version = '0.048',
    url = "http://code.google.com/p/gmapcatcher/",

    windows = [
                  {
                      'script': 'maps.py',
                      'icon_resources': [(1, "maps.ico")],
                  }
              ],

    options = {
                  'py2exe': {
                      'packages':'encodings',
                      'includes': 'cairo, pango, pangocairo, atk, gobject',
                  }
              },

    data_files=[
                   'Changelog',
                   'README'
               ]
)
