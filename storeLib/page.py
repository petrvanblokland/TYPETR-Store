#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# -----------------------------------------------------------------------------
#
import codecs
from random import shuffle

from storeLib.element import Element
from storeLib.image import IMAGES_EXT
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

    def getFileName(self):
        return self.name.lower().replace(' ', '-')

    def build(self, exportPath):
        self.buildContent()
        f = codecs.open(f'{exportPath}{self.getFileName()}.html', 'w', encoding='UTF-8')
        f.write(self.html)
        f.close()

    def buildContent(self):
        template = self.readTemplate(self.templateName) # Initialize self.html
        #self.html = template.format(page=self, site=self.site)
        self.html = ''
        for p1 in template.split('{{'):
            p2 = p1.split('}}')
            if len(p2) == 1:
                self.html += p2[0]
            else:
                self.html += eval(p2[0], dict(page=self, site=self.site))
                self.html += p2[1]

    #   C O N T E N T  F U N C T I O N S

    def _get_quickBrownFox(self):
        """Answer a unique “Quick Brown Fox” line, based on the global quickBrownFoxIndex"""
        global quickBrownFoxIndex
        if quickBrownFoxIndex > len(QUICK_BROWN_FOXES):
            quickBrownFoxIndex = 0
        qbf = QUICK_BROWN_FOXES[quickBrownFoxIndex]
        quickBrownFoxIndex += 1
        return qbf
    quickBrownFox = property(_get_quickBrownFox)

    #   L O G O

    def _get_logo(self):
        """Answer logo image object."""
        return self.site.findImage('type-try-logo')
    logo = property(_get_logo)

    #   P A G E  T I T L E

    def _get_pageTitle(self, pages):
        return self.name
    pageTitle = property(_get_pageTitle)

    #   M E N U

    def _get_menuPageLinks(self):
        html = ''
        for page in self.site.pages:
            html += f'\t\t<li><a href="{page.name.lower()}.html">{page.name}</a></li>\n'
        return html
    menuPageLinks = property(_get_menuPageLinks)

    #   F O N T S

    def _get_familyName(self):
        return self.site.fonts[self.slug].familyName
    familyName = property(_get_familyName)

    def _get_familySummary(self):
        html = ''
        font = self.site.fonts[self.slug]
        summary = font.content.get('familySummary')
        if summary is not None:
            html += f"""
            <div class="block">  
                <div class="one-colum">  
                    <p class="summary">{summary.text}</p>
                </div>
            </div>    
        """
        return html
    familySummary = property(_get_familySummary)

    def _get_articleText(self):
        html = ''
        article = None
        font = self.site.fonts[self.slug]
        for key, content in sorted(font.content.items()):
            if 'articleText' in key:
                article = content
        if article is not None:
            html = f"""
            <div class="block">  
              <div class="one-colum">  
                <div class="article">  
                  <div class="text-block">
                    {article.text}
                  </div>
                </div>     
              </div>
            </div>    
            """
        return html
    articleText = property(_get_articleText)

    def _get_articleTextImage(self):
        html = ''
        article = None
        font = self.site.fonts[self.slug]
        for key, content in sorted(font.content.items()):
            if 'articleTextImage' in key:
                article = content
        if article is not None:
            html = f"""
            <div class="two-colum flex"> 
              <div class="container-flex">
                <div class="column-flex">
                  <div class="text-block">
                    <div class="flux">
                      <p>{article.text}</p>
                    </div>
                  </div>
                </div>
                <div class="column-flex">
                  <div class="rot">
                    <img src="{self.site.findImage(article.images[0]).path}" class="sticky">
                    <figcaption>{article.captions[0]}</figcaption>
                  </div>
                </div>
              </div>
            </div>
            <hr>
            """
        return html
    articleTextImage = property(_get_articleTextImage)

    #   S L I D E  S H O W


    def _get_slideShow(self):
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
    slideShow = property(_get_slideShow)

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

    #    F O O T E R

    def _get_footer(self):
        return f"""
    <footer class="footer">
        <div class="footer-content">
            <div class="footer-logo">
                <a class="logo"> <img src="{self.logo.path}" alt="Logo" width="50%"/></a>
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
    footer = property(_get_footer)

    #   P R O M O

    def fontPromo(self, slug, imageRight=True, typeTester=False, buyButton=True, characterViewer=False, randomImage=True, style=None,
            head=None, headSize=None, subhead=None, subheadSize=None, deck=None,):
        if style is None:
            style = 'Regular'
        if slug not in self.site.fonts:
            print('###### Cannot find slug', slug)
            return

        font = self.site.fonts[slug]
        image = self.site.findPromoImage(font, doRandom=randomImage)

        html = ''
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

        html += f"""
        <div class="box">
          <div class="fontSample promo">
        """

        if not imageRight:
            html += f"""
              <div class="{side2}" style="background-image: url('{image.path}'); background-size: cover;background-position: center"
                onClick="window.location='{font.pageName}';">
              </div> <!-- side -->
=            """
        if 0 and not imageRight:
            html += f"""
              <div class="{side2}" width="500px" height="200px" style="overflow: hidden">
                  <img src="{image.path}" width="100%" height="100%" style="object-fit: cover"/>
                </a>
              </div> <!-- side -->
            """
        html += f"""
              <div class="{side1}">
                <div class="text">
                  <h2 style="font-family:{font.cssName};{headSize}">{head}</h2>
                  <h3 style="font-family:{font.cssName};{subheadSize} line-height:140%">{self.quickBrownFox}</h3>
                  <p>{deck} {'aaaaaa<br>' * 5}</p>
        """
        if buyButton:
            html += f"""<fontdue-buy-button collection-slug="{font.slug}"></fontdue-buy-button>"""
        html += f"""
                </div>
              </div> <!-- side1 -->
        """
        if imageRight:
            html += f"""
              <div class="{side2}" style="background-image: url('{image.path}'); background-size: cover;background-position: center"
                onClick="window.location='{font.pageName}';">
              </div> <!-- side -->
            """

        if typeTester or characterViewer:
            html += f"""
                  <div class="fontdueBox" style="font-family:{font.familyName}">AAAAAAAAAAå
                """
            if typeTester:
                html += f"""<fontdue-type-testers collection-slug="{font.slug}"></fontdue-type-testers>"""
                if buyButton:
                    html += f"""<fontdue-buy-button collection-slug="{font.slug}"></fontdue-buy-button>"""
            if characterViewer:
                html += f"""<fontdue-character-viewer collection-slug="{font.slug}"></fontdue-character-viewer>"""

            html += """
                </div> <!-- fontdue -->           
            """

        html += """
          </div> <!-- fontSample -->
        </div> <!-- box -->
        """
        return html

    def familyInfo(self, slug, imageRight=True, typeTester=False, buyButton=True, characterViewer=False, randomImage=True, style=None,
            head=None, headSize=None, subhead=None, subheadSize=None, deck=None,):
        if style is None:
            style = 'Regular'
        if slug not in self.site.fonts:
            print('###### Cannot find slug', slug)
            return

        font = self.site.fonts[slug]
        image = self.site.findPromoImage(font, doRandom=randomImage)

        html = ''
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


        html += f"""
        <div class="box">
          <div class="fontSample familyInfo">
        """

        if not imageRight:
            html += f"""
              <div class="{side2}" style="background-image: url('{image.path}'); background-size: cover;background-position: center">
              </div> <!-- side -->
            """
        if 0 and not imageRight:
            html += f"""
              <div class="{side2}" width="500px" height="200px" style="overflow: hidden">
                  <img src="{image.path}" width="100%" height="100%" style="object-fit: cover"/>
              </div> <!-- side -->
            """
        html += f"""
              <div class="{side1}">
                <div class="text">
                  <h2 style="font-family:{font.cssName} {style};{headSize}">{head}</h2>
                  <h3 style="font-family:{font.cssName} {style};{subheadSize}">An awesome font{subhead}</h3>
                  <p>{deck} {'aaaaaa<br>' * 10}</p>
        """
        if buyButton:
            html += f"""<fontdue-buy-button collection-slug="{font.slug}"></fontdue-buy-button>"""
        html += f"""
                </div>
              </div> <!-- side1 -->
        """
        if imageRight:
            html += f"""
              <div class="{side2}" style="background-image: url('{image.path}'); background-size: cover;background-position: center">
              </div> <!-- side -->
            """

        if typeTester or characterViewer:
            html += f"""
                  <div class="fontdueBox" style="font-family:{font.familyName} {style}">
                """
            if typeTester:
                html += f"""<fontdue-type-testers collection-slug="{font.slug}"></fontdue-type-testers>"""
                if buyButton:
                    self.html += f"""<fontdue-buy-button collection-slug="{font.slug}"></fontdue-buy-button>"""
            if characterViewer:
                html += f"""<fontdue-character-viewer collection-slug="{font.slug}"></fontdue-character-viewer>"""

            html += """
                </div> <!-- fontdue -->           
            """

        html += """
          </div> <!-- fontSample -->
        </div> <!-- box -->
        """
        return html

