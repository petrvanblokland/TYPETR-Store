#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# -----------------------------------------------------------------------------
#
from storeLib.element import Element
from storeLib.slugs import *

from storeLib.content.presti import CONTENT_PRESTI
from storeLib.content.upgrade import CONTENT_UPGRADE

class Font(Element):
    """Hold meta-information on all fonts in the fontdue library, collections and single styles."""
    def __init__(self, name, familyName, slug, id, collection=None, style=None, asBody=True):
        self.name = name
        self.familyName = familyName # Filter name to collect relevant images.
        self.style = style or 'Regular'
        self.slug = slug
        self.id = id
        if collection is None:
            collection = slug.startswith('tp-') # Otherwise try to interpret from the slug naming convention.
        self.collection = collection
        self.content = {}
        
    def _get_cssName(self):
        return f"""{self.name.replace('_', ' ').replace('TP ', '')}"""
    cssName = property(_get_cssName)

    def _get_imagePattern(self):
        return self.familyName.lower().replace('_', '-').replace(' ', '-')
    imagePattern = property(_get_imagePattern)

    def _get_pageName(self):
        return self.familyName.lower().replace(' ', '-') + '.html'
    pageName = property(_get_pageName)


