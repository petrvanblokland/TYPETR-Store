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
import weakref
from PIL import Image as PilImage
from random import shuffle

URL = 'typetr.com'

DO_BUILD = True

ASSETS_PATH = 'assets/'
TEMPLATES_PATH = 'templates/'
IMAGES_PATH = 'images/'
IMAGES_PATHS = [IMAGES_PATH]
for year in range(2018, 2026):
    IMAGES_PATHS.append(f'{IMAGES_PATH}{year}/')

if os.path.exists('_docs/'):
    EXPORT_PATH = '_docs/' # Jasper computer
    MAMP_PATH = '/Applications/MAMP/htdocs/typetr'
else:
    EXPORT_PATH = 'docs/'
    MAMP_PATH = '/Users/petr/Sites/localhost/typetr' # Petr computer

IMAGES_EXT = ('.jpg', '.jpeg', '.png', '.gif')

# Slugs used for family/font id

TP_PRESTI = 'tp-presti'
PRESTI_VF = 'presti-vf'
PRESTI_DISPLAY = 'presti-display'
PRESTI_HEAD = 'presti-head'
PRESTI_DECK = 'presti-deck'
PRESTI_TEXT = 'presti-text'
PRESTI_SMALL = 'presti-small'

TP_POWERLIFT = 'tp-powerlift'
POWERLIFT = 'powerlift'

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

class Element:

    def _get_site(self):
        if self._site is not None:
            return self._site()
        return None
    def _set_site(self, site):
        if site is not None:
            self._site = weakref.ref(site)
        else:
            self._site = None
    site = property(_get_site, _set_site)

class Font(Element):
    """Hold meta-information on all fonts in the fontdue library, collections and single styles."""
    def __init__(self, name, familyName, slug, id, collection=None, site=None, style=None):
        self.name = name
        self.familyName = familyName # Filter name to collect relevant images.
        self.style = style or 'Regular'
        self.slug = slug
        self.id = id
        if collection is None:
            collection = slug.startswith('tp-') # Otherwise try to interpret from the slug naming convention.
        self.collection = collection
        self.site = site # Set as weakref to the parent site

    def _get_cssName(self):
        return f"""{self.name.replace('_', ' ').replace('TP ', '')}"""
    cssName = property(_get_cssName)

    def _get_imagePattern(self):
        return self.familyName.lower().replace('_', '-').replace(' ', '-')
    imagePattern = property(_get_imagePattern)
    
class Image(Element):
    """Holds meta information about each image."""
    def __init__(self, path, type=None, site=None, slug=None):
        self.path = path
        if not os.path.exists(path):
            print(f'### Image path {path} does not exist')
            self.width = self.height = None
        else:
            self.name = path.split('/')[-1]
            im = PilImage.open(path)
            self.width, self.height = im.size
        self.type = type
        self.site = site # Set as weakref to the parent site
        self.slug = slug

class Page(Element):

    def __init__(self, name, slug=None, templateName=None, id=None, collectionSlug=None, site=None):
        self.name = name    
        self.slug = slug or 'tp-presti'
        self.templateName = templateName or name
        self.id = id or name
        self.collectionSlug = collectionSlug or ''
        self.html = None # Initialize by self.readTemplate(self.templateName)
        self.site = site # Set as weakref to the parent site

    def readTemplate(self, templateName):
        f = codecs.open(f'{TEMPLATES_PATH}{templateName}.html', 'r', encoding='UTF-8')
        template = f.read()
        f.close()
        return template

    # Content methods

    def getCollectionSlug(self):
        return self.collectionSlug

    def XXXXgetSlideShow(self):
        # Find relevant images
        imageNames = []
        allImageNames = []
        for imagesPath in IMAGES_PATHS:
            for fileName in sorted(os.listdir(imagesPath)):
                if not fileName.endswith(IMAGES_EXT):
                    continue
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

    def getSlideShow(self):
        html = """
        <div class="slideshow-container">
          <div class="slideshow">
        """
        images = self.site.findImages() # Find all images
        imagePaths = list(images.keys())
        shuffle(imagePaths)
        while len(imagePaths) < 10:
            imagePaths += imagePaths
        for imagePath in imagePaths[:10]:
            html += f'<div class="slide"><img src="{imagePath}" alt="Slide {imagePath}"></div>\n' 
        html += '</div></div>'
    
        return html

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

    def getFooter(self):
        logo = self.site.findImage('type-try-logo')

        self.html += f"""
    <footer class="footer">
        <div class="footer-content">
            <div class="footer-logo">
                <a class="logo"> <img src="{logo.path}" alt="Logo" width="50%"/></a>
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

    def menuPageLinks(self):
        html = ''
        for page in self.site.pages:
            html += f'\t\t<li><a href="{page.name.lower()}.html">{page.name}</a></li>\n'
        return html

    def buildContent(self):
        html = self.readTemplate(self.templateName) # Initialize self.html

        # First do simple replacements on the template
        for key, content in self.site.content.items():
            if hasattr(self, content):
                content = getattr(self, content)()
            elif hasattr(self, key): # Does it exist a method, then do the call.
                content = getattr(self, key)()
            html = html.replace('{{' + key + '}}', content)

        self.html = ''

        # Split the remaining {{python}} and execute the commands. The called functions then can fill in the html
        for start in html.split('{{'):
            stop = start.split('}}')
            if len(stop) == 2:
                exec(stop[0], {}, dict(site=self.site, page=self)) # Should add their html to page.html
                self.html += stop[1]
            elif len(stop) == 1:
                self.html += stop[0]

    def getFileName(self):
        return self.name.lower().replace(' ', '-')

    def build(self):
        self.buildContent()
        f = codecs.open(f'{EXPORT_PATH}{self.getFileName()}.html', 'w', encoding='UTF-8')
        f.write(self.html)
        f.close()

    def fontPromo(self, slug, imageRight=True, typeTester=False, buyButton=True, characterViewer=False, randomImage=True, style=None,
            head=None, headSize=None, subhead=None, subheadSize=None, deck=None,):
        if style is None:
            style = 'Regular'
        font = self.site.fonts[slug]
        image = self.site.findPromoImage(font, doRandom=randomImage)

        if head is None:
            head = font.familyName
        if headSize is not None:
            headSize = f'font-size:{headSize};'
        if subhead is None:
            subhead = '###'
        if subheadSize is not None:
            subheadSize = f'font-size:{subheadSize};'
        if deck is None:
            deck = '@@@@@'

        if imageRight:
            side1 = 'left'
            side2 = 'right'
        else:
            side1 = 'right'
            side2 = 'left'


        self.html += f"""
        <div class="box">
          <div class="fontSample">
        """

        if not imageRight:
            self.html += f"""
              <div class="{side2}" style="background-image: url('{image.path}'); background-size: cover;background-position: center">
              </div> <!-- side -->
            """
        if 0 and not imageRight:
            self.html += f"""
              <div class="{side2}" width="500px" height="200px" style="overflow: hidden">
                  <img src="{image.path}" width="100%" height="100%" style="object-fit: cover"/>
              </div> <!-- side -->
            """
        self.html += f"""
              <div class="{side1}">
                <div class="text">
                  <h2 style="font-family:{font.cssName} {style};{headSize}">{head}</h2>
                  <h3 style="font-family:{font.cssName} {style};{subheadSize}">{subhead}</h3>
                  <p>{deck} {'aaaaaa<br>' * 10}</p>
        """
        if buyButton:
            self.html += f"""<fontdue-buy-button collection-slug="{font.slug}"></fontdue-buy-button>"""
        self.html += f"""
                </div>
              </div> <!-- side1 -->
        """
        if imageRight:
            self.html += f"""
              <div class="{side2}" style="background-image: url('{image.path}'); background-size: cover;background-position: center">
              </div> <!-- side -->
            """
        if typeTester or characterViewer:
            self.html += f"""
                  <div style="font-family:{font.familyName} {style}">
                """
            if typeTester:
                self.html += f"""<fontdue-type-testers collection-slug="{font.slug}"></fontdue-type-testers>"""
                if buyButton:
                    self.html += f"""<fontdue-buy-button collection-slug="{font.slug}"></fontdue-buy-button>"""
            if characterViewer:
                self.html += f"""<fontdue-character-viewer collection-slug="{font.slug}"></fontdue-character-viewer>"""

            self.html += """
                </div> <!-- fontdue -->           
            """

        self.html += """
          </div> <!-- fontSample -->
        </div> <!-- box -->
        """

class Site:

    def __init__(self, url, id):
        self.url = url
        self.id = id
        self.initializeFonts()
        self.initializeImages()
        self.initializePages()

    def initializeFonts(self):
        # Copying Fontdue data here, since font id's are not likely to changed easily.
        # Key is the slug-id of the font in the fontdue database.
        self.fonts = {
            TP_PRESTI:              Font(name='TP Presti', site=self, familyName='Presti', slug=TP_PRESTI, id='Rm9udENvbGxlY3Rpb246MTkyMDQ3OTcwMDEwMzg5OTcyMg=='),
            PRESTI_VF:              Font(name='Presti VF', site=self, familyName='Presti', slug=PRESTI_VF, id='Rm9udENvbGxlY3Rpb246MTkyMDQ3OTc4MjM2MjU4OTc3Nw=='),
            PRESTI_DISPLAY:         Font(name='Presti Display', site=self, familyName='Presti', slug=PRESTI_DISPLAY, id='Rm9udENvbGxlY3Rpb246MTkyMDQ4MDM2NDg2NzUyOTI5OA=='),
            PRESTI_HEAD:            Font(name='Presti Head', site=self, familyName='Presti', slug=PRESTI_HEAD, id='Rm9udENvbGxlY3Rpb246MTkyMDQ4MzU4Mzc5NDUyMjc3MA=='),
            PRESTI_DECK:            Font(name='Presti Deck', site=self, familyName='Presti', slug=PRESTI_DECK, id='Rm9udENvbGxlY3Rpb246MTkyMDQ4NDIwOTIwNzE5MjI1Nw=='),
            PRESTI_TEXT:            Font(name='Presti Text', site=self, familyName='Presti', slug=PRESTI_DECK, id='Rm9udENvbGxlY3Rpb246MTkyMDQ4NDUxMTg5MzMzNDc2OA=='),
            PRESTI_SMALL:           Font(name='Presti Small', site=self, familyName='Presti', slug=PRESTI_SMALL, id='Rm9udENvbGxlY3Rpb246MTkyMDQ4NDc0OTIwNzA1NTEzNQ=='),

            TP_POWERLIFT:           Font(name='TP PowerLift', site=self, familyName='PowerLift', slug=TP_POWERLIFT, id='Rm9udENvbGxlY3Rpb246MTkyMDQ4NTAyOTI0Mzk1NjA0Ng=='),
            POWERLIFT:              Font(name='PowerLift', site=self, familyName='PowerLift', slug=POWERLIFT, id='Rm9udENvbGxlY3Rpb246MTkyMDQ4NTEzMjQ1NzM4ODg4NQ=='),

            TP_PRODUCTUS:           Font(name='TP Productus', site=self, familyName='Productus', slug=TP_PRODUCTUS, id='Rm9udENvbGxlY3Rpb246MTkyMDQ4OTA3MzQ1MDU5MzExOQ=='),
            PRODUCTUS:              Font(name='Productus', site=self, familyName='Productus', slug=PRODUCTUS, id='Rm9udENvbGxlY3Rpb246MTkyMDQ4OTE0MDgxMTExNTM4Mg=='),

            TP_PROFORMA:            Font(name='TP Proforma', site=self, familyName='Proforma', slug=TP_PROFORMA, id='Rm9udENvbGxlY3Rpb246MTkyMDQ5MzE4MTc4ODEzODM2Mg=='),
            PROFORMA:               Font(name='Proforma', site=self, familyName='Proforma', slug=PROFORMA, id='Rm9udENvbGxlY3Rpb246MTkyMDQ5MzI5Mjk1Mzk3MTYyOQ=='),

            TP_RESPONDER_P:         Font(name='TP Responder P', site=self, familyName='Responder P', slug=TP_RESPONDER_P, id='Rm9udENvbGxlY3Rpb246MTkyMDQ5NDE3NzEzODQyMDY1Nw=='),
            RESPONDER_P_VF:         Font(name='Responder P VF', site=self, familyName='Responder P', slug=RESPONDER_P_VF, id='Rm9udENvbGxlY3Rpb246MTkyMDQ5NDE4MDMzNDQ4MDM0NQ=='),
            RESPONDER_P:            Font(name='Responder P', site=self, familyName='Responder P', slug=RESPONDER_P, id='Rm9udENvbGxlY3Rpb246MTkyMDQ5NDE3NzE2MzU4NjQ4Mw=='),

            TP_UPGRADE:             Font(name='TP Upgrade', site=self, familyName='Upgrade', slug=TP_UPGRADE, id='Rm9udENvbGxlY3Rpb246MTkyMDQ5NDg4MjQ2OTM1ODU2MA=='),
            UPGRADE:                Font(name='Upgrade]', site=self, familyName='Upgrade', slug=UPGRADE, id='Rm9udENvbGxlY3Rpb246MTkyMDQ5NTAxMjU0MzExMzIzNQ=='),

            TP_BITCOUNT_GRID:       Font(name='TP Bitcount Grid', site=self, familyName='Bitcount', slug=TP_BITCOUNT_GRID, id='Rm9udENvbGxlY3Rpb246MTkyMDQ5NjEyNTY0NDI4NTk3NQ=='),
            BITCOUNT_GRID_DOUBLE:   Font(name='Bitcount Grid Double]', site=self, familyName='Bitcount', slug=BITCOUNT_GRID_DOUBLE, id='Rm9udENvbGxlY3Rpb246MTkyMDQ5NjEyNTY2MTA2MzE5Mw=='),
            BITCOUNT_GRID_SINGLE:   Font(name='Bitcount Grid Single]', site=self, familyName='Bitcount', slug=BITCOUNT_GRID_SINGLE, id='Rm9udENvbGxlY3Rpb246MTkyMDQ5NjEyNzMwNTIzMDQ2Mw=='),

            TP_BITCOUNT_MONO:       Font(name='TP Bitcount Mono', site=self, familyName='Bitcount', slug=TP_BITCOUNT_MONO, id='Rm9udENvbGxlY3Rpb246MTkyMDQ5NjEyNTY0NDI4NTk3NQ=='),
            BITCOUNT_MONO_DOUBLE:   Font(name='Bitcount Mono Double]', site=self, familyName='Bitcount', slug=BITCOUNT_MONO_DOUBLE, id='Rm9udENvbGxlY3Rpb246MTkyMDQ5Nzk0NTI3NTk2NzcyNA=='),
            BITCOUNT_MONO_SINGLE:   Font(name='Bitcount Mono Single]', site=self, familyName='Bitcount', slug=BITCOUNT_MONO_SINGLE, id='Rm9udENvbGxlY3Rpb246MTkyMDQ5Nzk0ODAyNzQzMTI1MA=='),

            TP_BITCOUNT_PROP:       Font(name='TP Bitcount Prop', site=self, familyName='Bitcount', slug=TP_BITCOUNT_PROP, id='Rm9udENvbGxlY3Rpb246MTkyMDQ5OTMyMzg4NDk3MjQ3NQ=='),
            BITCOUNT_PROP_DOUBLE:   Font(name='Bitcount Prop Double]', site=self, familyName='Bitcount', slug=BITCOUNT_PROP_DOUBLE, id='Rm9udENvbGxlY3Rpb246MTkyMDQ5OTMyMzkxMDEzODMwMQ=='),
            BITCOUNT_PROP_SINGLE:   Font(name='Bitcount Prop Single]', site=self, familyName='Bitcount', slug=BITCOUNT_PROP_SINGLE, id='Rm9udENvbGxlY3Rpb246MTkyMDQ5OTMyNjUxMDYwNjg4Mw=='),
        }

        # Key values replace the {{key}} references in the templated-binary/index.html templates. 
        self.content = {
            'logo': '<img src="images/type-try-logo.gif" width="50%"/>',
            'menuPageLinks': 'menuPageLinks',
            'pageTitle': 'getPageTitle',
            'collection-slug': 'getCollectionSlug',
            'slideShow': 'getSlideShow',

            'bitcountImage': 'getBitcountImage'
        }  

    def initializeImages(self):
        # Find relevant images
        self.images = {} # Dictionary of Image instances, key is their unique path
        for imagesPath in IMAGES_PATHS:
            for fileName in sorted(os.listdir(imagesPath)):
                if not fileName.endswith(IMAGES_EXT):
                    continue
                imagePath = imagesPath + fileName
                self.images[imagePath] = Image(imagePath, site=self)

    def initializePages(self):
        self.pages = [] # Define as list, so there's a bit of ordering of pages
        for page in (
                Page('Index', templateName='index'),
                Page('About', templateName='index'),
                Page('Licensing', templateName='index'),
                Page('Contact', templateName='index'),
                Page('TYPETR in use', templateName='index'),

                Page('Presti', slug='tp-presti', templateName='index', collectionSlug='Presti Display'),
                Page('Proforma', slug='tp-proforma', templateName='index'),
                Page('Powerlift', slug='tp-powerlif', templateName='index'),
                Page('Responder', slug='tp-responder-vf', templateName='index'),
                Page('Upgrade', slug='tp-upgrade', templateName='index'),
                Page('Upgrade Neon', templateName='index'),
                Page('Upgrade Outline', templateName='index'),
                Page('About TYPETR', templateName='index'),
            ):
            self.pages.append(page)
            page.site = self # Make x-ref

    def findImages(self, slug=None, year=None, type=None):
        """Answer a dictionary of images that fit the defined filter values."""
        images = {}
        for imagePath, image in self.images.items():
            if slug == image.slug or year in image.year or type in image.type or (slug, year, type) == (None, None, None):
                images[imagePath] = image
        return images

    def findImage(self, pattern):
        """Find the first image in the sorted(self.images) that fits the pattern."""
        for imageName, image in sorted(self.images.items()):
            if pattern in image.name:
                return image

    def findPromoImage(self, font, doRandom=True):
        promoImages = []
        for imageName, image in self.images.items():
            print(font.imagePattern in image.path.lower(), font.familyName.lower(), image.path.lower(), )
            if font.imagePattern in image.path.lower():
                promoImages.append(image)
        if not promoImages: # Nothing found
            promoImages = [self.findImage('Logo')]
        if doRandom:
            shuffle(promoImages)
        return promoImages[0]

    def copyDir(self, path1, path2):
        shutil.copytree(path1, path2)

    def build(self):
        if os.path.exists(EXPORT_PATH):
            shutil.rmtree(EXPORT_PATH)
            os.mkdir(EXPORT_PATH)

        self.copyDir(ASSETS_PATH, EXPORT_PATH + ASSETS_PATH)
        self.copyDir(IMAGES_PATH, EXPORT_PATH + IMAGES_PATH)

        for page in self.pages:
            page.build()

        # Write the CNAME file
        f = codecs.open(f'{EXPORT_PATH}CNAME', 'w', encoding='UTF-8')
        f.write(URL)
        f.close()

#PORT = 8888
PORT = 80

if DO_BUILD:
    site = Site('typetr', 'typetr')

    site.build()

if MAMP_PATH is not None:
    # Start MAMP to see this website on localhost, port 80
    # Since we modify the 'docs/', better make a tree copy than exporting again.
    mampPath = MAMP_PATH #+ site.id
    if os.path.exists(mampPath):
        print('... Remove old site at', mampPath)
        shutil.rmtree(mampPath)
    shutil.copytree(EXPORT_PATH, mampPath)
    #website.export(mampPath)

    # Open the local website on docs/, assuming that MAMP is running
    os.system(u'/usr/bin/open %s/%s' % (site.url, site.id))

print('Done')