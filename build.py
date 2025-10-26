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
#   https://tonka-tests.vercel.app/?rows=10&cols=9&weights=100%2C200%2C300%2C400%2C458%2C524%2C600%2C660%2C726%2C800&widths=1%2C28%2C55%2C85%2C100%2C130%2C190%2C250%2C300
#
#   https://store.typetr.com/
#   petrvanblokland.github.io
#   https://render.com/docs/static-sites
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
    # Local site is available at http://localhost/typetr/index.html
    mampPath = MAMP_PATH #+ site.id
    if os.path.exists(mampPath):
        print('... Remove old site at', mampPath)
        os.system(f"rm  -r  {MAMP_PATH}") #/Applications/MAMP/htdocs/typetr")
    print(f'... Copy {EXPORT_PATH} to {mampPath}')
    shutil.copytree(EXPORT_PATH, mampPath)

docsPath = 'docs/'
if os.path.exists(docsPath):
    print('... Remove old site at', docsPath)
    os.system(f"rm  -r  {docsPath}") #/Applications/MAMP/htdocs/typetr")
print(f'... Copy {EXPORT_PATH} to {docsPath}')
shutil.copytree(EXPORT_PATH, docsPath)

os.system('echo "type-try.com" >docs/CNAME')

    # Open the local website on docs/, assuming that MAMP is running
    #os.system(u'/usr/bin/open %s/%s' % (site.name, site.id))

print('Done')
