#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# -----------------------------------------------------------------------------
#
#   T Y P E T R . C O M
#
#   Copyright (c) 2020+ Buro Petr van Blokland + Claudia Mens
#
#   build.py
#
#   Source builds the type-try.com website using PageBotNano the Website 
#   publication class.
#
#   https://docs.fontdue.com
#   https://typetr.fontdue.com/admin/settings/website
#
#   http://localhost/typetr/index.html
#   https://petrvanblokland.github.io/TYPETR-Store/index.html
#
#   Content examples
#   https://upgrade.typenetwork.com
#
import os, shutil

from random import shuffle

from lib.site import Site
from lib.page import Page
from lib.font import Font
from lib.image import Image
from lib.slugs import *

URL = 'typetr.com'

DO_BUILD = True

ASSETS_PATH = 'assets/'
TEMPLATES_PATH = 'templates/'
IMAGES_PATH = 'images/' # Root path of all images

if os.path.exists('/Users/jaspervanblokland'):
    EXPORT_PATH = '_docs/' # Jasper computer
    MAMP_PATH = '/Applications/MAMP/htdocs/typetr'
elif os.path.exists('/Users/petr'):
    EXPORT_PATH = 'docs/'
    MAMP_PATH = '/Users/petr/Sites/localhost/typetr/' # Petr computer


#PORT = 8888
PORT = 80

if DO_BUILD:
    site = Site('typetr', 'typetr', URL, IMAGES_PATH, ASSETS_PATH, TEMPLATES_PATH)

    site.build(EXPORT_PATH)

if MAMP_PATH is not None:
    # Start MAMP to see this website on localhost, port 80
    # Since we modify the 'docs/', better make a tree copy than exporting again.
    mampPath = MAMP_PATH #+ site.id
    if os.path.exists(mampPath):
        print('... Remove old site at', mampPath)
        os.system(f"rm  -r  {MAMP_PATH}") #/Applications/MAMP/htdocs/typetr")
    shutil.copytree(EXPORT_PATH, mampPath)

    # Open the local website on docs/, assuming that MAMP is running
    os.system(u'/usr/bin/open %s/%s' % (site.name, site.id))

print('Done')
