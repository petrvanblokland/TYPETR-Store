#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# -----------------------------------------------------------------------------
#
from content.element import Element
from content.slugs import *

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

def getFonts(site):
    """Construct the font elements. Store the weakref to site in the font element.
    Store all corresponding Fontdue unique ID‘s for each font element.
    """
    
    fonts = {
        TP_PRESTI:              Font(name='TP Presti', site=site, familyName='Presti', slug=TP_PRESTI, id='Rm9udENvbGxlY3Rpb246MTkyMDQ3OTcwMDEwMzg5OTcyMg=='),
        PRESTI_VF:              Font(name='Presti VF', site=site, familyName='Presti', slug=PRESTI_VF, id='Rm9udENvbGxlY3Rpb246MTkyMDQ3OTc4MjM2MjU4OTc3Nw=='),
        PRESTI_DISPLAY:         Font(name='Presti Display', site=site, familyName='Presti', slug=PRESTI_DISPLAY, id='Rm9udENvbGxlY3Rpb246MTkyMDQ4MDM2NDg2NzUyOTI5OA=='),
        PRESTI_HEAD:            Font(name='Presti Head', site=site, familyName='Presti', slug=PRESTI_HEAD, id='Rm9udENvbGxlY3Rpb246MTkyMDQ4MzU4Mzc5NDUyMjc3MA=='),
        PRESTI_DECK:            Font(name='Presti Deck', site=site, familyName='Presti', slug=PRESTI_DECK, id='Rm9udENvbGxlY3Rpb246MTkyMDQ4NDIwOTIwNzE5MjI1Nw=='),
        PRESTI_TEXT:            Font(name='Presti Text', site=site, familyName='Presti', slug=PRESTI_DECK, id='Rm9udENvbGxlY3Rpb246MTkyMDQ4NDUxMTg5MzMzNDc2OA=='),
        PRESTI_SMALL:           Font(name='Presti Small', site=site, familyName='Presti', slug=PRESTI_SMALL, id='Rm9udENvbGxlY3Rpb246MTkyMDQ4NDc0OTIwNzA1NTEzNQ=='),

        TP_POWERLIFT:           Font(name='TP PowerLift', site=site, familyName='PowerLift', slug=TP_POWERLIFT, id='Rm9udENvbGxlY3Rpb246MTkyMDQ4NTAyOTI0Mzk1NjA0Ng=='),
        POWERLIFT:              Font(name='PowerLift', site=site, familyName='PowerLift', slug=POWERLIFT, id='Rm9udENvbGxlY3Rpb246MTkyMDQ4NTEzMjQ1NzM4ODg4NQ=='),

        TP_PRODUCTUS:           Font(name='TP Productus', site=site, familyName='Productus', slug=TP_PRODUCTUS, id='Rm9udENvbGxlY3Rpb246MTkyMDQ4OTA3MzQ1MDU5MzExOQ=='),
        PRODUCTUS:              Font(name='Productus', site=site, familyName='Productus', slug=PRODUCTUS, id='Rm9udENvbGxlY3Rpb246MTkyMDQ4OTE0MDgxMTExNTM4Mg=='),

        TP_PROFORMA:            Font(name='TP Proforma', site=site, familyName='Proforma', slug=TP_PROFORMA, id='Rm9udENvbGxlY3Rpb246MTkyMDQ5MzE4MTc4ODEzODM2Mg=='),
        PROFORMA:               Font(name='Proforma', site=site, familyName='Proforma', slug=PROFORMA, id='Rm9udENvbGxlY3Rpb246MTkyMDQ5MzI5Mjk1Mzk3MTYyOQ=='),

        TP_RESPONDER_P:         Font(name='TP Responder P', site=site, familyName='Responder P', slug=TP_RESPONDER_P, id='Rm9udENvbGxlY3Rpb246MTkyMDQ5NDE3NzEzODQyMDY1Nw=='),
        RESPONDER_P_VF:         Font(name='Responder P VF', site=site, familyName='Responder P', slug=RESPONDER_P_VF, id='Rm9udENvbGxlY3Rpb246MTkyMDQ5NDE4MDMzNDQ4MDM0NQ=='),
        RESPONDER_P:            Font(name='Responder P', site=site, familyName='Responder P', slug=RESPONDER_P, id='Rm9udENvbGxlY3Rpb246MTkyMDQ5NDE3NzE2MzU4NjQ4Mw=='),

        TP_UPGRADE:             Font(name='TP Upgrade', site=site, familyName='Upgrade', slug=TP_UPGRADE, id='Rm9udENvbGxlY3Rpb246MTkyMDQ5NDg4MjQ2OTM1ODU2MA=='),
        UPGRADE:                Font(name='Upgrade]', site=site, familyName='Upgrade', slug=UPGRADE, id='Rm9udENvbGxlY3Rpb246MTkyMDQ5NTAxMjU0MzExMzIzNQ=='),

        TP_BITCOUNT_GRID:       Font(name='TP Bitcount Grid', site=site, familyName='Bitcount', slug=TP_BITCOUNT_GRID, id='Rm9udENvbGxlY3Rpb246MTkyMDQ5NjEyNTY0NDI4NTk3NQ=='),
        BITCOUNT_GRID_DOUBLE:   Font(name='Bitcount Grid Double]', site=site, familyName='Bitcount', slug=BITCOUNT_GRID_DOUBLE, id='Rm9udENvbGxlY3Rpb246MTkyMDQ5NjEyNTY2MTA2MzE5Mw=='),
        BITCOUNT_GRID_SINGLE:   Font(name='Bitcount Grid Single]', site=site, familyName='Bitcount', slug=BITCOUNT_GRID_SINGLE, id='Rm9udENvbGxlY3Rpb246MTkyMDQ5NjEyNzMwNTIzMDQ2Mw=='),

        TP_BITCOUNT_MONO:       Font(name='TP Bitcount Mono', site=site, familyName='Bitcount', slug=TP_BITCOUNT_MONO, id='Rm9udENvbGxlY3Rpb246MTkyMDQ5NjEyNTY0NDI4NTk3NQ=='),
        BITCOUNT_MONO_DOUBLE:   Font(name='Bitcount Mono Double]', site=site, familyName='Bitcount', slug=BITCOUNT_MONO_DOUBLE, id='Rm9udENvbGxlY3Rpb246MTkyMDQ5Nzk0NTI3NTk2NzcyNA=='),
        BITCOUNT_MONO_SINGLE:   Font(name='Bitcount Mono Single]', site=site, familyName='Bitcount', slug=BITCOUNT_MONO_SINGLE, id='Rm9udENvbGxlY3Rpb246MTkyMDQ5Nzk0ODAyNzQzMTI1MA=='),

        TP_BITCOUNT_PROP:       Font(name='TP Bitcount Prop', site=site, familyName='Bitcount', slug=TP_BITCOUNT_PROP, id='Rm9udENvbGxlY3Rpb246MTkyMDQ5OTMyMzg4NDk3MjQ3NQ=='),
        BITCOUNT_PROP_DOUBLE:   Font(name='Bitcount Prop Double]', site=site, familyName='Bitcount', slug=BITCOUNT_PROP_DOUBLE, id='Rm9udENvbGxlY3Rpb246MTkyMDQ5OTMyMzkxMDEzODMwMQ=='),
        BITCOUNT_PROP_SINGLE:   Font(name='Bitcount Prop Single]', site=site, familyName='Bitcount', slug=BITCOUNT_PROP_SINGLE, id='Rm9udENvbGxlY3Rpb246MTkyMDQ5OTMyNjUxMDYwNjg4Mw=='),
    }
    return fonts


