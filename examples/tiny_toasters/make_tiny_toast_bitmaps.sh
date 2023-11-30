#!/bin/sh

../../utils/sprites_converter.py tiny_toasters.bmp 32 32 3 > tiny_toasters_bitmaps.py
# mpy-cross tiny_toasters_bitmaps.py
# mpremote cp tiny_toasters_bitmaps.mpy :
