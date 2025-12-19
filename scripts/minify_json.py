#!/usr/bin/env python3

import os
"""
    Minifies json outputs for system tests
    Uses third party tool jsmin
    Useful for testing and makes files smaller
"""

# need third party minifier
try:
    from jsmin import jsmin
except:
    print("Requires third party lib - jsmin, do 'pip3 install jsmin'")


filename = 'test93'
file_ext = 'json'

#loop over dirs and input files
print("Processing file: {}".format(filename))
with open("{}.{}".format(filename, file_ext)) as js_file:
    with open("{}.min.{}".format(filename, file_ext), "w") as min_file:
        min_file.write(jsmin(js_file.read()))
