#!/usr/bin/python

""" Basic script for fetching facebook profile image from a given user."""

import urllib.request as rq
import sys

username = sys.argv[1]
url = 'https://graph.facebook.com/' + username + '/picture?type=large'
fig_resp = rq.urlopen(url).read()

image_file = username + '.jpg'
f = open (image_file, 'wb')
f.write(fig_resp)
f.close()

print ('File saved successfully.')
