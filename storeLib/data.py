#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# -----------------------------------------------------------------------------
#
#   Main storage of all constants of the site
#
import os

from storeLib.font import Font
from storeLib.slugs import *

URL = 'typetr.com'

ASSETS_PATH = 'assets/'
TEMPLATES_PATH = 'templates/'
IMAGES_PATH = 'images/' # Root path of all images

if os.path.exists('/Users/jaspervanblokland'):
    EXPORT_PATH = '_docs/' # Jasper computer
    MAMP_PATH = '/Applications/MAMP/htdocs/typetr'
elif os.path.exists('/Users/petr'):
    EXPORT_PATH = 'docs/'
    MAMP_PATH = '/Users/petr/Sites/localhost/typetr/' # Petr computer

FONTS = {
    # P R E S T I

    TP_PRESTI:       
        Font(name='TP Presti', 
            familyName='Presti', 
            slug=TP_PRESTI,
            id='Rm9udENvbGxlY3Rpb246MTkyMDQ3OTcwMDEwMzg5OTcyMg=='),

    PRESTI_VF: 
        Font(name='Presti VF', 
            familyName='Presti', 
            slug=PRESTI_VF, id='Rm9udENvbGxlY3Rpb246MTkyMDQ3OTc4MjM2MjU4OTc3Nw=='),

    PRESTI_DISPLAY:
        Font(name='Presti Display', 
            familyName='Presti', 
            slug=PRESTI_DISPLAY, 
            id='Rm9udENvbGxlY3Rpb246MTkyMDQ4MDM2NDg2NzUyOTI5OA=='),

    PRESTI_HEAD:            
        Font(name='Presti Head', 
            familyName='Presti', 
            slug=PRESTI_HEAD, 
            id='Rm9udENvbGxlY3Rpb246MTkyMDQ4MzU4Mzc5NDUyMjc3MA=='),

    PRESTI_DECK:
        Font(name='Presti Deck', 
            familyName='Presti', 
            slug=PRESTI_DECK, 
            id='Rm9udENvbGxlY3Rpb246MTkyMDQ4NDIwOTIwNzE5MjI1Nw=='),

    PRESTI_TEXT:
        Font(name='Presti Text', 
            familyName='Presti', 
            slug=PRESTI_DECK, 
            id='Rm9udENvbGxlY3Rpb246MTkyMDQ4NDUxMTg5MzMzNDc2OA=='),

    PRESTI_SMALL:
        Font(name='Presti Small', 
            familyName='Presti', 
            slug=PRESTI_SMALL, 
            id='Rm9udENvbGxlY3Rpb246MTkyMDQ4NDc0OTIwNzA1NTEzNQ=='),

    # P O W E R L I F T

    TP_POWERLIFT:
        Font(name='TP PowerLift', 
            familyName='PowerLift', 
            slug=TP_POWERLIFT, 
            id='Rm9udENvbGxlY3Rpb246MTkyMDQ4NTAyOTI0Mzk1NjA0Ng==',
            asBody=False),

    POWERLIFT:
        Font(name='PowerLift', 
            familyName='PowerLift', 
            slug=POWERLIFT, 
            id='Rm9udENvbGxlY3Rpb246MTkyMDQ4NTEzMjQ1NzM4ODg4NQ==',
            asBody=False),

    # P R O D U C T U S

    TP_PRODUCTUS:
        Font(name='TP Productus', 
            familyName='Productus', 
            slug=TP_PRODUCTUS, 
            id='Rm9udENvbGxlY3Rpb246MTkyMDQ4OTA3MzQ1MDU5MzExOQ=='),

    PRODUCTUS:
        Font(name='Productus', 
            familyName='Productus', 
            slug=PRODUCTUS, 
            id='Rm9udENvbGxlY3Rpb246MTkyMDQ4OTE0MDgxMTExNTM4Mg=='),

    # P R O F O R M A

    TP_PROFORMA:
        Font(name='TP Proforma', 
            familyName='Proforma', 
            slug=TP_PROFORMA, 
            id='Rm9udENvbGxlY3Rpb246MTkyMDQ5MzE4MTc4ODEzODM2Mg=='),

    PROFORMA:
        Font(name='Proforma', 
            familyName='Proforma', 
            slug=PROFORMA, 
            id='Rm9udENvbGxlY3Rpb246MTkyMDQ5MzI5Mjk1Mzk3MTYyOQ=='),

    # P R O F O R M A  P R O

    # R E S P O N D E R  P

    TP_RESPONDER_P:         
        Font(name='TP Responder P', 
            familyName='Responder P', 
            slug=TP_RESPONDER_P, 
            id='Rm9udENvbGxlY3Rpb246MTkyMDQ5NDE3NzEzODQyMDY1Nw=='),

    RESPONDER_P_VF:         
        Font(name='Responder P VF', 
            familyName='Responder P', 
            slug=RESPONDER_P_VF, 
            id='Rm9udENvbGxlY3Rpb246MTkyMDQ5NDE4MDMzNDQ4MDM0NQ=='),

    RESPONDER_P:            
        Font(name='Responder P', 
            familyName='Responder P', 
            slug=RESPONDER_P, 
            id='Rm9udENvbGxlY3Rpb246MTkyMDQ5NDE3NzE2MzU4NjQ4Mw=='),

    # U P G R A D E

    TP_UPGRADE:             
        Font(name='TP Upgrade', 
            familyName='Upgrade', 
            slug=TP_UPGRADE, 
            id='Rm9udENvbGxlY3Rpb246MTkyMDQ5NDg4MjQ2OTM1ODU2MA=='),

    UPGRADE:
        Font(name='Upgrade]', 
            familyName='Upgrade', 
            slug=UPGRADE, 
            id='Rm9udENvbGxlY3Rpb246MTkyMDQ5NTAxMjU0MzExMzIzNQ=='),

    # B I T C O U N T

    TP_BITCOUNT_GRID:       
        Font(name='TP Bitcount Grid', 
            familyName='Bitcount', 
            slug=TP_BITCOUNT_GRID, 
            id='Rm9udENvbGxlY3Rpb246MTkyMDQ5NjEyNTY0NDI4NTk3NQ=='),

    BITCOUNT_GRID_DOUBLE:   
        Font(name='Bitcount Grid Double]', 
            familyName='Bitcount', 
            slug=BITCOUNT_GRID_DOUBLE, 
            id='Rm9udENvbGxlY3Rpb246MTkyMDQ5NjEyNTY2MTA2MzE5Mw=='),

    BITCOUNT_GRID_SINGLE:   
        Font(name='Bitcount Grid Single]', 
            familyName='Bitcount', 
            slug=BITCOUNT_GRID_SINGLE, 
            id='Rm9udENvbGxlY3Rpb246MTkyMDQ5NjEyNzMwNTIzMDQ2Mw=='),

    TP_BITCOUNT_MONO:       
        Font(name='TP Bitcount Mono', 
            familyName='Bitcount', 
            slug=TP_BITCOUNT_MONO, 
            id='Rm9udENvbGxlY3Rpb246MTkyMDQ5NjEyNTY0NDI4NTk3NQ=='),

    BITCOUNT_MONO_DOUBLE:   
        Font(name='Bitcount Mono Double]', 
            familyName='Bitcount', 
            slug=BITCOUNT_MONO_DOUBLE, 
            id='Rm9udENvbGxlY3Rpb246MTkyMDQ5Nzk0NTI3NTk2NzcyNA=='),

    BITCOUNT_MONO_SINGLE:   
        Font(name='Bitcount Mono Single]', 
            familyName='Bitcount', 
            slug=BITCOUNT_MONO_SINGLE, 
            id='Rm9udENvbGxlY3Rpb246MTkyMDQ5Nzk0ODAyNzQzMTI1MA=='),

    TP_BITCOUNT_PROP:       
        Font(name='TP Bitcount Prop', 
            familyName='Bitcount', 
            slug=TP_BITCOUNT_PROP, 
            id='Rm9udENvbGxlY3Rpb246MTkyMDQ5OTMyMzg4NDk3MjQ3NQ=='),

    BITCOUNT_PROP_DOUBLE:   
        Font(name='Bitcount Prop Double]', 
            familyName='Bitcount', 
            slug=BITCOUNT_PROP_DOUBLE, 
            id='Rm9udENvbGxlY3Rpb246MTkyMDQ5OTMyMzkxMDEzODMwMQ=='),

    BITCOUNT_PROP_SINGLE:   
        Font(name='Bitcount Prop Single]', 
            familyName='Bitcount', 
            slug=BITCOUNT_PROP_SINGLE, 
            id='Rm9udENvbGxlY3Rpb246MTkyMDQ5OTMyNjUxMDYwNjg4Mw=='),
}


