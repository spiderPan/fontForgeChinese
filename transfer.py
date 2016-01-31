#!/usr/bin/python
# -*- coding: utf-8 -*-
import codecs
import urllib
import urllib2
import os.path

filePath = 'fan.txt'
REQUEST_HEADERS = {
"Accept-Language": "en-US,en;q=0.5",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
"Referer": "http://thewebsite.com",
"Connection": "keep-alive" 
}

def download_file(url, folder='image'):
    if not os.path.exists(folder):
        os.makedirs(folder)

    filename = url.split('/')[-1]
    complete_filename = os.path.join(folder, filename)
    try:
        u = urllib2.urlopen(url)
        req = urllib2.Request(url, headers=REQUEST_HEADERS)
        handle = urllib2.urlopen(req)
    except urllib2.HTTPError, e:
        print 'We failed with error code - %s.' % e.code
        return False

    data = handle.read()

    with open(complete_filename, 'wb') as f:
        f.write(data)
        print 'success'

    return True
	
with codecs.open(filePath, 'r', 'utf-8') as f:
    while True:
        c = f.read(1)
        if not c:
            print 'End of file'
            break
        url = 'http://sampler.linotype.com/sam/sam?ID=1390633^&text=' \
            + c.encode('utf-8') + '^&sizex=4000^&sizey=4000^&fontsize=3000'
        url = urllib.quote(url.encode('utf-8'))
        download_file(url)
        print 'Read a character:', c
        print 'URL:', url






			