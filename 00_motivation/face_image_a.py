#!/usr/bin/python

""" More advanced script for fetching facebook profile image from a given user."""

import threading
import urllib.request as rq

import sys
import time

def fetch_image(user):
    image_url = 'https://graph.facebook.com/{0}/picture?type=large'.format(user)
    image_resp = rq.urlopen(image_url).read()
    image_file = '{0}.jpg'.format(user)
    f = open (image_file, 'wb')
    f.write(image_resp)
    f.close()

username = sys.argv[1]
thread = threading.Thread(target=fetch_image, args=(username,))

charlist = ['|', '/', '-', '\\']
c = 1
sys.stdout.write('Downloading... |')
sys.stdout.flush()
thread.start()
while thread.is_alive():
    sys.stdout.write("\b{0}".format( charlist[c % 4] ))
    c += 1
    sys.stdout.flush()
    time.sleep(.15)

sys.stdout.write("\b \n")
sys.stdout.flush()
print('Done.')
