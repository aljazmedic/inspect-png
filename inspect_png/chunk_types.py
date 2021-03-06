#!/usr/bin/env python3

#https://github.com/Hedroed/png-parser/blob/master/pngparser/chunktypes.py

TYPE_IHDR = b'IHDR'
TYPE_PLTE = b'PLTE'
TYPE_IDAT = b'IDAT'
TYPE_IEND = b'IEND'
TYPE_bKGD = b'bKGD'
TYPE_cHRM = b'cHRM'
TYPE_dSIG = b'dSIG'
TYPE_eXIf = b'eXIf'
TYPE_gAMA = b'gAMA'
TYPE_hIST = b'hIST'
TYPE_iCCP = b'iCCP'
TYPE_iTXt = b'iTXt'
TYPE_pHYs = b'pHYs'
TYPE_sBIT = b'sBIT'
TYPE_sPLT = b'sPLT'
TYPE_sRGB = b'sRGB'
TYPE_sTER = b'sTER'
TYPE_tEXt = b'tEXt'
TYPE_tIME = b'tIME'
TYPE_tRNS = b'tRNS'
TYPE_zTXt = b'zTXt'

SPECIFIED_TYPES =  []
TEXT_CHUNKS = (TYPE_tEXt, TYPE_iTXt, TYPE_eXIf, TYPE_zTXt)
for k in list(filter(lambda x: x.startswith("TYPE_"), locals())):
    SPECIFIED_TYPES.append(locals()[k])

def is_not_specified(o):
    """ Checking if chunk is of a specified type (in contrast to non-specified)"""
    return o.ctype not in SPECIFIED_TYPES

def is_txt_chunk(o):
    """ Checks if o is a text chunk """
    return o.ctype in TEXT_CHUNKS
