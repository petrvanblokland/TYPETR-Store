#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# -----------------------------------------------------------------------------
#
import os, shutil, codecs
from random import shuffle

from storeLib.element import Element
from storeLib.page import Page
from storeLib.image import Image, IMAGES_EXT, IMAGES_START_YEAR, IMAGES_END_YEAR, IMAGES_DIRS
from storeLib.slugs import *

class Site:

    def __init__(self, name, id, url, fonts, imageRootPath, assetsPath, templatesPath, patterns=None):
        self.name = name
        self.id = id
        self.url = url
        self.imageRootPath = imageRootPath # Root
        self.assetsPath = assetsPath
        self.templatesPath = templatesPath
        self.fonts = fonts
        self.initializeImages()
        self.initializePages()

    def initializeImageDir(self, imageDirPath):    
        # Find relevant images
        for fileName in sorted(os.listdir(imageDirPath)):
            if not fileName.endswith(IMAGES_EXT):
                continue
            imagePath = imageDirPath + fileName
            self.images[imagePath] = Image(imagePath, site=self)

    def initializeImages(self):
        self.images = {} # Dictionary of Image instances, key is their unique path
        self.imageDirPaths = []
        for year in range(IMAGES_START_YEAR, IMAGES_END_YEAR):
            imageDirPath = f'{self.imageRootPath}{year}/'            
            self.imageDirPaths.append(imageDirPath)
            self.initializeImageDir(imageDirPath)
        for imageDirPath in IMAGES_DIRS:
            imageDirPath = self.imageRootPath + imageDirPath
            self.imageDirPaths.append(imageDirPath)
            self.initializeImageDir(imageDirPath)

    def initializePages(self):
        self.pages = [] # Define as list, so there's a bit of ordering of pages
        for page in (
                Page('Index', templateName='index'),
                Page('About', templateName='index'),
                Page('Licensing', templateName='index'),
                Page('Contact', templateName='index'),
                Page('TYPETR in use', templateName='index'),

                Page('Presti', slug=TP_PRESTI, templateName='family', collectionSlug='Presti Display'),
                Page('Proforma', slug=TP_PROFORMA, templateName='family'),
                Page('Powerlift', slug=TP_POWERLIFT, templateName='family'),
                Page('Responder-P', slug=TP_RESPONDER_P, templateName='family'),
                Page('Upgrade', slug=TP_UPGRADE, templateName='family'),
                
                #Page('Upgrade Neon', slug='???????', templateName='family'),
                #Page('Upgrade Outline', slug='???????', templateName='family'),
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
            #print(font.imagePattern in image.path.lower(), font.familyName.lower(), image.path.lower(), )
            if image.path is not None and font.imagePattern in image.path.lower():
                promoImages.append(image)
        if not promoImages: # Nothing found
            promoImages = [self.findImage('Logo')]
        if doRandom:
            shuffle(promoImages)
        return promoImages[0]

    def copyDir(self, path1, path2):
        shutil.copytree(path1, path2)

    def build(self, exportPath):
        if os.path.exists(exportPath):
            shutil.rmtree(exportPath)
            os.mkdir(exportPath)

        self.copyDir(self.assetsPath, exportPath + self.assetsPath)
        self.copyDir(self.imageRootPath, exportPath + self.imageRootPath)

        for page in self.pages:
            page.build(exportPath)

        # Write the CNAME file
        f = codecs.open(f'{exportPath}CNAME', 'w', encoding='UTF-8')
        f.write(self.url)
        f.close()
