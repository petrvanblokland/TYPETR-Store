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
#
import os, shutil, codecs
from PIL import Image as PilImage
from random import shuffle

URL = 'typetr.com'

DO_BUILD = True
USE_MAMP = True

# Slugs used for family/font id
UPGRADE = 'tp-upgrade'

EXPORT_PATH = 'docs/'
ASSETS_PATH = 'assets/'
IMAGES_PATH = 'images/'
MAMP_PATH = '/Users/petr/Sites/localhost/typetr'
TEMPLATE_PATH = 'templates/'

TP_PRESTI = 'tp-presti'
PRESTI_VF = 'presti-vf'
PRESTI_DISPLAY = 'presti-display'
PRESTI_HEAD = 'presti-head'
PRESTI_DECK = 'presti-deck'
PRESTI_TEXT = 'presti-text'
PRESTI_SMALL = 'presti-small'

TP_POWERLIFT = 'tp-powerLift'
POWERLIFT = 'powerLift'

TP_PRODUCTUS = 'tp-productus'
PRODUCTUS = 'productus'

TP_PROFORMA = 'tp-proforma'
PROFORMA = 'proforma'

TP_RESPONDER_P = 'tp-responde-p'
RESPONDER_P_VF = 'responder-p-vf'
RESPONDER_P = 'responder-p'

TP_UPGRADE = 'tp-upgrade'
UPGRADE = 'upgrade'

TP_BITCOUNT_GRID = 'tp-bitcount-grid'
BITCOUNT_GRID_DOUBLE = 'bitcount-grid-double'
BITCOUNT_GRID_SINGLE = 'bitcount-grid-single'

TP_BITCOUNT_MONO = 'tp-bitcount-mono'
BITCOUNT_MONO_DOUBLE = 'bitcount-mono-double'
BITCOUNT_MONO_SINGLE = 'bitcount-mono-single'

TP_BITCOUNT_PROP = 'tp-bitcount-prop'
BITCOUNT_PROP_DOUBLE = 'bitcount-prop-double'
BITCOUNT_PROP_SINGLE = 'bitcount-prop-single'


class Font:
    """Hold meta-information on all fonts in the fontdue library, collections and single styles."""
    def __init__(self, name, family, slug, id, collection=None):
        self.name = name
        self.family = family # Filter name to collect relevant images.
        self.slug = slug
        self.id = id
        if collection is None:
            collection = slug.startswith('tp-') # Otherwise try to interpret from the slug naming convention.
        self.collection = collection

class Image:
    """Holds meta information about each image."""
    def __init__(self, path):
        assert os.path.exists(path)
        self.path = path
        self.name = path.split('/')[-1]
        im = PilImage.open(path)
        self.width, self.height = im.size
        print(self.width, self.height, self.path)

# Copying Fontdue data here, since font id's are not likelt to changed easily.
FONTS = {
    TP_PRESTI:              Font(name='TP Presti', family='Presti', slug=TP_PRESTI, id='Rm9udENvbGxlY3Rpb246MTkyMDQ3OTcwMDEwMzg5OTcyMg=='),
    PRESTI_VF:              Font(name='Presti VF', family='Presti', slug=PRESTI_VF, id='Rm9udENvbGxlY3Rpb246MTkyMDQ3OTc4MjM2MjU4OTc3Nw=='),
    PRESTI_DISPLAY:         Font(name='Presti Display', family='Presti', slug=PRESTI_DISPLAY, id='Rm9udENvbGxlY3Rpb246MTkyMDQ4MDM2NDg2NzUyOTI5OA=='),
    PRESTI_HEAD:            Font(name='Presti Head', family='Presti', slug=PRESTI_HEAD, id='Rm9udENvbGxlY3Rpb246MTkyMDQ4MzU4Mzc5NDUyMjc3MA=='),
    PRESTI_DECK:            Font(name='Presti Deck', family='Presti', slug=PRESTI_DECK, id='Rm9udENvbGxlY3Rpb246MTkyMDQ4NDIwOTIwNzE5MjI1Nw=='),
    PRESTI_TEXT:            Font(name='Presti Text', family='Presti', slug=PRESTI_DECK, id='Rm9udENvbGxlY3Rpb246MTkyMDQ4NDUxMTg5MzMzNDc2OA=='),
    PRESTI_SMALL:           Font(name='Presti Small', family='Presti', slug=PRESTI_SMALL, id='Rm9udENvbGxlY3Rpb246MTkyMDQ4NDc0OTIwNzA1NTEzNQ=='),

    TP_POWERLIFT:           Font(name='TP PowerLift', family='PowerLift', slug=TP_POWERLIFT, id='Rm9udENvbGxlY3Rpb246MTkyMDQ4NTAyOTI0Mzk1NjA0Ng=='),
    POWERLIFT:              Font(name='PowerLift', family='PowerLift', slug=POWERLIFT, id='Rm9udENvbGxlY3Rpb246MTkyMDQ4NTEzMjQ1NzM4ODg4NQ=='),

    TP_PRODUCTUS:           Font(name='TP Productus', family='Productus', slug=TP_PRODUCTUS, id='Rm9udENvbGxlY3Rpb246MTkyMDQ4OTA3MzQ1MDU5MzExOQ=='),
    PRODUCTUS:              Font(name='Productus', family='Productus', slug=PRODUCTUS, id='Rm9udENvbGxlY3Rpb246MTkyMDQ4OTE0MDgxMTExNTM4Mg=='),

    TP_PROFORMA:            Font(name='TP Proforma', family='Proforma', slug=TP_PROFORMA, id='Rm9udENvbGxlY3Rpb246MTkyMDQ5MzE4MTc4ODEzODM2Mg=='),
    PROFORMA:               Font(name='Proforma', family='Proforma', slug=PROFORMA, id='Rm9udENvbGxlY3Rpb246MTkyMDQ5MzI5Mjk1Mzk3MTYyOQ=='),

    TP_RESPONDER_P:         Font(name='TP Responder P', family='ResponderP', slug=TP_RESPONDER_P, id='Rm9udENvbGxlY3Rpb246MTkyMDQ5NDE3NzEzODQyMDY1Nw=='),
    RESPONDER_P_VF:         Font(name='Responder P VF', family='ResponderP', slug=RESPONDER_P_VF, id='Rm9udENvbGxlY3Rpb246MTkyMDQ5NDE4MDMzNDQ4MDM0NQ=='),
    RESPONDER_P:            Font(name='Responder P', family='ResponderP', slug=RESPONDER_P, id='Rm9udENvbGxlY3Rpb246MTkyMDQ5NDE3NzE2MzU4NjQ4Mw=='),

    TP_UPGRADE:             Font(name='TP Upgrade', family='Upgrade', slug=TP_UPGRADE, id='Rm9udENvbGxlY3Rpb246MTkyMDQ5NDg4MjQ2OTM1ODU2MA=='),
    UPGRADE:                Font(name='Upgrade]', family='Upgrade', slug=UPGRADE, id='Rm9udENvbGxlY3Rpb246MTkyMDQ5NTAxMjU0MzExMzIzNQ=='),

    TP_BITCOUNT_GRID:       Font(name='TP Bitcount Grid', family='Bitcount', slug=TP_BITCOUNT_GRID, id='Rm9udENvbGxlY3Rpb246MTkyMDQ5NjEyNTY0NDI4NTk3NQ=='),
    BITCOUNT_GRID_DOUBLE:   Font(name='Bitcount Grid Double]', family='Bitcount', slug=BITCOUNT_GRID_DOUBLE, id='Rm9udENvbGxlY3Rpb246MTkyMDQ5NjEyNTY2MTA2MzE5Mw=='),
    BITCOUNT_GRID_SINGLE:   Font(name='Bitcount Grid Single]', family='Bitcount', slug=BITCOUNT_GRID_SINGLE, id='Rm9udENvbGxlY3Rpb246MTkyMDQ5NjEyNzMwNTIzMDQ2Mw=='),

    TP_BITCOUNT_MONO:       Font(name='TP Bitcount Mono', family='Bitcount', slug=TP_BITCOUNT_MONO, id='Rm9udENvbGxlY3Rpb246MTkyMDQ5NjEyNTY0NDI4NTk3NQ=='),
    BITCOUNT_MONO_DOUBLE:   Font(name='Bitcount Mono Double]', family='Bitcount', slug=BITCOUNT_MONO_DOUBLE, id='Rm9udENvbGxlY3Rpb246MTkyMDQ5Nzk0NTI3NTk2NzcyNA=='),
    BITCOUNT_MONO_SINGLE:   Font(name='Bitcount Mono Single]', family='Bitcount', slug=BITCOUNT_MONO_SINGLE, id='Rm9udENvbGxlY3Rpb246MTkyMDQ5Nzk0ODAyNzQzMTI1MA=='),

    TP_BITCOUNT_PROP:       Font(name='TP Bitcount Prop', family='Bitcount', slug=TP_BITCOUNT_PROP, id='Rm9udENvbGxlY3Rpb246MTkyMDQ5OTMyMzg4NDk3MjQ3NQ=='),
    BITCOUNT_PROP_DOUBLE:   Font(name='Bitcount Prop Double]', family='Bitcount', slug=BITCOUNT_PROP_DOUBLE, id='Rm9udENvbGxlY3Rpb246MTkyMDQ5OTMyMzkxMDEzODMwMQ=='),
    BITCOUNT_PROP_SINGLE:   Font(name='Bitcount Prop Single]', family='Bitcount', slug=BITCOUNT_PROP_SINGLE, id='Rm9udENvbGxlY3Rpb246MTkyMDQ5OTMyNjUxMDYwNjg4Mw=='),
}

# Key values replace the {{key}} references in the templated-binary/index.html templates. 
CONTENT = {
    'logo': '<img src="images/type-try-logo.gif" width="50%"/>',
    'menuPageLinks': 'menuPageLinks',
    'pageTitle': 'getPageTitle',
    'collection-slug': 'getCollectionSlug',
    'slideShow': 'getSlideShow',
    'footer': 'getFooter',

    'bitcountImage': 'getBitcountImage'
}  

class Page:

    def __init__(self, name, slug=None, templateName=None, id=None, collectionSlug=None):
        self.name = name    
        self.slug = slug or 'tp-presti'
        self.templateName = templateName or name
        self.id = id or name
        self.collectionSlug = collectionSlug or ''
        self.findImages() # Make an inventory of all available images into a self.images dictionary. Key is fontname, value is list of file names.
        self.readTemplate(self.templateName)

    def readTemplate(self, templateName):
        f = codecs.open(f'{TEMPLATE_PATH}{templateName}.html', 'r', encoding='UTF-8')
        self.html = f.read()
        f.close()

    # Content methods

    def getPageTitle(self, pages):
        return self.name

    def getCollectionSlug(self, pages):
        return self.collectionSlug

    def findImages(self):
        self.images = {}

    def getSlideShow(self, pages):
        # Find relevant images
        imageNames = []
        allImageNames = []
        html = []
        tag = self.name.replace(' ', '_')
        for year in (2022, 2023, 2024):
            imagesPath = f'images/{year}/'
            for fileName in sorted(os.listdir(imagesPath)):
                imagePath = imagesPath + fileName
                allImageNames.append((year, fileName))
                if tag in fileName:
                    im = Image(imagePath)
                    imageNames.append((year, fileName))
        if not imageNames:
            imageNames = allImageNames
        while len(imageNames) < 10:
            imageNames += imageNames + imageNames
        shuffle(imageNames)
        for year, imageName in imageNames:
            if imageName.split('.')[-1] in ('jpg', 'png', 'gif'):
                html.append(f'<div class="slide"><img src="images/{year}/{imageName}" alt="Slide {imageName}"></div>')

        return '\n'.join(html)

    def XXXgetSlideShow(self, pages):
        html = ["""
        <div class="slideshow-container">
          <div class="slideshow">
        """]
        htmlImages = []
        imageNames = []
        allImageNames = []
        tag = self.name.replace(' ', '_')
        for fileName in sorted(os.listdir('images/2022/')):
            allImageNames.append(fileName)
            if tag in fileName:
                imageNames.append(fileName)
        if not imageNames:
            imageNames = allImageNames
        while len(imageNames) < 10: # Not enough images, then duplicate the list
            imageNames += imageNames + imageNames
        for imageName in imageNames:
            if imageName.split('.')[-1] in ('jpg', 'png', 'gif'):
                htmlImages.append(f'<div class="slide"><img src="images/2022/{imageName}" alt="Slide {imageName}"></div>')

        # Duplicate first slide for smooth transition
        htmlImages.append(htmlImages[0])
        html += htmlImages
        html.append('</div></div>')
    
        return '\n'.join(html)

    def getCssSlideShowKeyFrames(self, pages):
        """
        @keyframes slideShow {
  {{slideShowKeyFrames}}
  0% { transform: translateX(0); }
  10% { transform: translateX(-100%); }
  20% { transform: translateX(-200%); }
  30% { transform: translateX(-300%); }
  40% { transform: translateX(-400%); }
  50% { transform: translateX(-500%); }
  60% { transform: translateX(-600%); }
  70% { transform: translateX(-700%); }
  80% { transform: translateX(-800%); }
  90% { transform: translateX(-900%); }
  100% { transform: translateX(0); }
}
    """

    def getFooter(self, pages):
        html = """
    <footer class="footer">
        <div class="footer-content">
            <div class="footer-logo">
                <img src="images/type-try-logo.gif" alt="Logo" width="50%"/>
            </div>
            <div class="footer-links">
                <ul>
                    <li><a href="contact.html">Contact</a></li>
                    <li><a href="about.html">About</a></li>
                    <li><a href="licensing.html">Licensing</a></li>
                    <li><a href="usage.html">Usage</a></li>
                </ul>
            </div>
        </div>
    </footer>
    """
        return html

    def menuPageLinks(self, pages):
        html = ''
        for page in pages:
            html += f'\t\t<li><a href="{page.name.lower()}.html">{page.name}</a></li>\n'
        return html

    def buildContent(self, pages):
        for key, content in CONTENT.items():
            if hasattr(self, content):
                content = getattr(self, content)(pages)
            elif hasattr(self, key): # Does it exist a method, then do the call.
                content = getattr(self, key)(pages)
            
            self.html = self.html.replace('{{' + key + '}}', content)

    def getFileName(self):
        return self.name.lower().replace(' ', '-')

    def build(self, pages):
        self.buildContent(pages)
        f = codecs.open(f'{EXPORT_PATH}{self.getFileName()}.html', 'w', encoding='UTF-8')
        f.write(self.html)
        f.close()

class Site:

    def __init__(self, url, id):
        self.url = url
        self.id = id
        self.pages = []

    def appendPage(self, page):
        self.pages.append(page)

    def copyDir(self, path1, path2):
        shutil.copytree(path1, path2)

    def build(self):
        if os.path.exists(EXPORT_PATH):
            shutil.rmtree(EXPORT_PATH)
            os.mkdir(EXPORT_PATH)

        self.copyDir(ASSETS_PATH, EXPORT_PATH + ASSETS_PATH)
        self.copyDir(IMAGES_PATH, EXPORT_PATH + IMAGES_PATH)

        for page in self.pages:
            page.build(self.pages)

        # Write the CNAME file
        f = codecs.open(f'{EXPORT_PATH}CNAME', 'w', encoding='UTF-8')
        f.write(URL)
        f.close()

#PORT = 8888
PORT = 80

if DO_BUILD:
    site = Site('typetr', 'typetr')

    # Pagename, template name
    site.appendPage(Page('Index', templateName='index'))
    site.appendPage(Page('About', templateName='index'))
    site.appendPage(Page('Licensing', templateName='index'))
    site.appendPage(Page('Contact', templateName='index'))
    site.appendPage(Page('TYPETR in use', templateName='index'))

    site.appendPage(Page('Presti', slug='tp-presti', templateName='index', collectionSlug='Presti Display'))
    site.appendPage(Page('Proforma Pro', slug='tp-proforma', templateName='index'))
    site.appendPage(Page('Powerlift', slug='tp-powerlif', templateName='index'))
    site.appendPage(Page('Responder', slug='tp-responder', templateName='index'))
    site.appendPage(Page('Upgrade', slug='tp-upgrade', templateName='index'))
    site.appendPage(Page('Upgrade Neon', templateName='index'))
    site.appendPage(Page('Upgrade Outline', templateName='index'))
    site.appendPage(Page('About TYPETR', templateName='index'))

    site.build()

if USE_MAMP:
    # Start MAMP to see this website on localhost, port 80
    # Since we modify the 'docs/', better make a tree copy than exporting again.
    mampPath = MAMP_PATH #+ site.id
    if os.path.exists(mampPath):
        print('... Remove old site at', mampPath)
        shutil.rmtree(mampPath)
    shutil.copytree('docs/', mampPath)
    #website.export(mampPath)

    # Open the local website on docs/, assuming that MAMP is running
    os.system(u'/usr/bin/open %s/%s' % (site.url, site.id))

print('Done')