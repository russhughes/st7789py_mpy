#!/bin/sh

../../utils/image_converter.py alien.png 1 >alien_bitmap.py

# mpy-cross alien_bitmap.py
# mpremote cp alien_bitmap.mpy :
# mpremote run alien.py
