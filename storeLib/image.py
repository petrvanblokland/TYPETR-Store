#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# -----------------------------------------------------------------------------
#
import os
from PIL import Image as PilImage

from storeLib.element import Element

IMAGES_EXT = ('.jpg', '.jpeg', '.png', '.gif')
IMAGES_DIRS = ('logos/',)

IMAGES_START_YEAR = 2018
IMAGES_END_YEAR = 2026

class Image(Element):
    """Holds meta information about each image."""
    def __init__(self, path, type=None, site=None, slug=None):
        self._path = path
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

    def _get_path(self):
        return self._path
    def _set_path(self, path):
        self._path = path
    path = property(_get_path)