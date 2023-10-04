# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 13:08:20 2023

@author: tiwashima
"""

import base64

print(base64.urlsafe_b64encode("What you want as B64".encode()).decode().strip("="))
