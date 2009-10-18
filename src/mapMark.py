## @package src.mapMark
# Read and Write the locations of the Markers

import os
import re
import gtk
import fileUtils
import mapPixbuf
from mapConst import *

class MyMarkers:
    # coord = (lat, lng, zoom_level)
    positions = {}

    def refresh(self):
        self.positions = {}
        self.read_markers()

    def read_markers(self):
        self.positions = fileUtils.read_file('marker', self.markerPath)

    def write_markers(self):
        fileUtils.write_file('marker', self.markerPath, self.positions)

    def __init__(self, configpath=None):
        localPath = os.path.expanduser(configpath or DEFAULT_PATH)
        self.markerPath = os.path.join(localPath, 'markers')

        if not os.path.isdir(localPath):
            os.mkdir(localPath)

        if (os.path.exists(self.markerPath)):
            self.read_markers()
        else:
            self.write_markers()

    def get_markers(self):
        return self.positions

    def get_pixDim(self, zl):
        maxZoom = MAP_MAX_ZOOM_LEVEL - 2
        if zl >= maxZoom :
            return 56
        elif zl <= 1:
            return 256
        else:
            return 56 + int((maxZoom - zl) * 15)

    def get_marker_pixbuf(self, zl):
        pixDim = self.get_pixDim(zl)
        return mapPixbuf.getImage('marker.png', pixDim, pixDim)
