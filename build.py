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

from storeLib.data import FONTS, URL, IMAGES_PATH, ASSETS_PATH, TEMPLATES_PATH, MAMP_PATH, EXPORT_PATH

DO_BUILD = True


#PORT = 8888
PORT = 80

EXPORT_PATH = TEMPLATES_PATH

if DO_BUILD:
    #site = Site('typetr', 'typetr', URL, FONTS, IMAGES_PATH, ASSETS_PATH, TEMPLATES_PATH)
    #site.build(EXPORT_PATH)
    pass
    
if MAMP_PATH is not None:
    # Start MAMP to see this website on localhost, port 80
    # Since we modify the 'docs/', better make a tree copy than exporting again.
    mampPath = MAMP_PATH #+ site.id
    if os.path.exists(mampPath):
        print('... Remove old site at', mampPath)
        os.system(f"rm  -r  {MAMP_PATH}") #/Applications/MAMP/htdocs/typetr")
    print(f'... Copy {EXPORT_PATH} to {mampPath}')
    shutil.copytree(EXPORT_PATH, mampPath)

    docsPath = 'docs/'
    if os.path.exists(mampPath):
        print('... Remove old site at', docsPath)
        os.system(f"rm  -r  {docsPath}") #/Applications/MAMP/htdocs/typetr")
    print(f'... Copy {EXPORT_PATH} to {docsPath}')
    shutil.copytree(EXPORT_PATH, docsPath)

    # Open the local website on docs/, assuming that MAMP is running
    #os.system(u'/usr/bin/open %s/%s' % (site.name, site.id))

print('Done')
