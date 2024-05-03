#!/usr/bin/env python3
# -----------------------------------------------------------------------------
# file: main.py
# Created on : 2024-04-23
# by : Roland Deschain
#
#
#
# --- imports -----------------------------------------------------------------
import bpy
from PIL import Image

from blenderhelloworld.import_test import test

for some_object in bpy.data.objects:
    print(some_object.name)
    image = Image.new("RGB", (100, 50))
    print(image)
    test()
    print("done")
