#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# -----------------------------------------------------------------------------
#
import codecs
from random import shuffle

from content.element import Element
from content.image import IMAGES_EXT
from content.quick_brown_foxes import QUICK_BROWN_FOXES

quickBrownFoxIndex = 0 # Index to get unique random quick brown fox sentences.

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
        f = codecs.open(f'{self.site.templatesPath}{templateName}.html', 'r', encoding='UTF-8')
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
        for key, pattern in self.site.patterns.items():
            if hasattr(self, pattern):
                pattern = getattr(self, pattern)()
            elif hasattr(self, key): # Does it exist a method, then do the call.
                pattern = getattr(self, key)()
            html = html.replace('{{' + key + '}}', pattern)

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

    def build(self, exportPath):
        self.buildContent()
        f = codecs.open(f'{exportPath}{self.getFileName()}.html', 'w', encoding='UTF-8')
        f.write(self.html)
        f.close()

    def getQuickBrowFox(self):
        """Answer a unique “Quick Brown Fox” line, based on the global quickBrownFoxIndex"""
        global quickBrownFoxIndex
        if quickBrownFoxIndex > len(QUICK_BROWN_FOXES):
            quickBrownFoxIndex = 0
        qbf = QUICK_BROWN_FOXES[quickBrownFoxIndex]
        quickBrownFoxIndex += 1
        return qbf

    def fontPromo(self, slug, imageRight=True, typeTester=False, buyButton=True, characterViewer=False, randomImage=True, style=None,
            head=None, headSize=None, subhead=None, subheadSize=None, deck=None,):
        if style is None:
            style = 'Regular'
        if slug not in self.site.fonts:
            print('###### Cannot find slug', slug)
            return

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
          <div class="fontSample promo">
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
                  <h3 style="font-family:{font.cssName} {style};{subheadSize} line-height:140%">{self.getQuickBrowFox()}</h3>
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
                  <div class="fontdueBox" style="font-family:{font.familyName} {style}">
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

    def familyInfo(self, slug, imageRight=True, typeTester=False, buyButton=True, characterViewer=False, randomImage=True, style=None,
            head=None, headSize=None, subhead=None, subheadSize=None, deck=None,):
        if style is None:
            style = 'Regular'
        if slug not in self.site.fonts:
            print('###### Cannot find slug', slug)
            return

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
          <div class="fontSample familyInfo">
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
                  <h3 style="font-family:{font.cssName} {style};{subheadSize}">An awesome font{subhead}</h3>
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
                  <div class="fontdueBox" style="font-family:{font.familyName} {style}">
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
