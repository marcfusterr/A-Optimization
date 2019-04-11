#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 19:47:32 2018

@author: Carlos y Marc
"""

import argparse
import webbrowser
import os
import gmplot


# Place map in Albacete
gmap = gmplot.GoogleMapPlotter(38.993464, -1.859774, 7)

# Select input file
input_file = 'output_a_star_haversine.txt'

# Define an output file name according to input file name
output_file = input_file.split('.')[-2] + ".html"

# Read coordinates from input_file
latitude = []
longitude = []
with open(input_file, 'r') as f:
    for line in f:
        if line.startswith("#"):
            continue
        fields = line.split('|')
        for field in fields:
            field.strip()
        latitude.append(float(fields[3]))
        longitude.append(float(fields[4]))

# Add route to map
gmap.plot(latitude, longitude, 'cornflowerblue', edge_width=6)

# Save map
gmap.draw(output_file)

# Show map
f = webbrowser.open("file://" + os.path.realpath(output_file))


