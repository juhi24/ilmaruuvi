#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Jussi Tiira
"""
import base64

def decode(b64):
    decoded64 = base64.urlsafe_b64decode(b64)
    fmt = decoded64[0]
    if fmt==2:
        rh = decoded64[1]*0.5
        utemp = ((decoded64[2] & 127) << 8)|decoded64[3]
        stemp = (decoded64[2] >> 7) & 1
        temp = utemp/256 if stemp == 0 else utemp/-256
        pres = (((decoded64[4] << 8) + decoded64[5]) + 50000)/100
    return {'temperature': temp, 'pressure': pres, 'humidity': rh}

