# -*- coding: utf-8 -*-
# Converted from Chango-Regular.ttf using:
#     ./font2bitmap.py Chango-Regular.ttf 16 -c 0x20-0x7f

# Maps the order of the character data
MAP = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"

# Number of color bits per pixel, currently only 1 is used but could be
# increased to support antialiased or smoothed fonts in the future.
BPP = 1

# Font height
HEIGHT = 17

# Font max width
MAX_WIDTH = 24

# one byte per character table of widths in the same order as the MAP string
_WIDTHS = \
    b'\x06\x08\x0a\x0e\x0d\x18\x10\x06\x08\x08\x0a\x0d\x06\x08\x06\x0b'\

    ... more lines of data...

    b'\x0d\x0d\x0b\x0a\x0b\x0e\x0c\x12\x0d\x0c\x0b\x09\x06\x09\x0e\x0b'

# OFFSET_WIDTH bytes per character in the same order as the MAP string
# to the start of each character in bits.
OFFSET_WIDTH = 2
_OFFSETS = \
    b'\x00\x00\x00\x66\x00\xee\x01\x98\x02\x86\x03\x63\x04\xfb\x06\x0b'\

    ... more lines of data...

    b'\x49\x94\x4a\x71\x4b\x3d\x4b\xf8\x4c\x91\x4c\xf7\x4d\x90\x4e\x7e'

# character bitmaps per character in the same order as the MAP string.
# Note: character data may not start on byte boundaries
_BITMAPS =\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x61'\

    ... many more lines of data...

    b'\x3d\xe3\xfc\x00\x00\x00\x00\x00'

WIDTHS = memoryview(_WIDTHS)
OFFSETS = memoryview(_OFFSETS)
BITMAPS = memoryview(_BITMAPS)
