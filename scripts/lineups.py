#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 01:00:18 2017

@author: malcolmng
"""

try:
    import Image
except ImportError:
    from PIL import Image
    import pytesseract
    print(pytesseract.image_to_string(Image.open('Screenshot.png')))
    
