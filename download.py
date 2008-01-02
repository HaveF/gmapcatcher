#!/usr/bin/env python
import os
import gobject
import pygtk
import gtk
import googleMaps
import sys

ctx_map = googleMaps.GoogleMaps()
max_zl = 17
min_zl = 3

def download(lat, lng, lat_range, lng_range):
	lat_min = lat - lat_range
	lat_max = lat + lat_range
	lng_min = lng - lng_range
	lng_max = lng + lng_range
	
	for zl in range(max_zl, min_zl, -1):
		print "Downloading zl %d" % zl
		tlx, tly = ctx_map.coord_to_tile(zl, lat_max, lng_min)
		brx, bry = ctx_map.coord_to_tile(zl, lat_min, lng_max)
		for x in range(tlx, brx+1):
			for y in range(tly, bry+1):
				ctx_map.get_file(zl, (x, y), True)

if __name__ == "__main__":
	lat = None
	lng = None
	location = None
	lat_range = 0.1
	lng_range = 0.1

	if len(sys.argv) > 1:
		for arg in sys.argv[1:]:
			if arg.startswith('--'):
				if arg.startswith('--max-zoom-level='):
					max_zl = int(arg[17:])
				if arg.startswith('--min-zoom-level='):
					min_zl = int(arg[17:])
				if arg.startswith('--location='):
					location = arg[11:]
				if arg.startswith('--longitude='):
					lng = float(arg[12:])
				if arg.startswith('--latitude='):
					lat = float(arg[11:])
				if arg.startswith('--latrange='):
					lat_range = float(arg[11:])
				if arg.startswith('--lngrange='):
					lng_range = float(arg[11:])

	if (location == None) and ((lat == None) or (lng == None)):
		print 'use --location set location'
		print 'or --longitude and --latitude'
		exit(0)
	print "location = %s" % location
	if ((lat == None) or (lng == None)):
		locations = ctx_map.get_locations()
		if (not location in locations.keys()):
			l = ctx_map.search_location(location)
			if (False == l):
				print "Can't find %s in google map" % location
				exit(0)
			location = l;
		lat, lng = ctx_map.get_locations()[location]
	if (location == None):
		location = "somewhere"
	print "Download %s (%f, %f), range (%f, %f), scale: (%d, %d)" % (location, lat, lng, lat_range, lng_range,
			max_zl, min_zl)
	download(lat, lng, lat_range, lng_range)

