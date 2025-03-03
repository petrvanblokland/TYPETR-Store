#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# -----------------------------------------------------------------------------
#
import weakref

class Element:
    """Base root class for all other element classes.
    """

    # Add the site attribute as weakref, so all elements have access to all other elenents.
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
