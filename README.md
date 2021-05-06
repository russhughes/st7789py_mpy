Python ST7789 driver for MicroPython
====================================

This is a fork of devbis' st7789py_mpy module from
https://github.com/devbis/st7789py_mpy.

This driver adds support for:

- 320x240, 240x240 and 135x240 pixel displays
- Display rotation
- Hardware based scrolling
- Drawing text using 8 and 16 bit wide bitmap fonts with heights that are
  multiples of 8.  Included are 12 bitmap fonts derived from classic pc
  BIOS text mode fonts.
- Drawing text using converted TrueType fonts.
- Drawing converted bitmaps

This is a work in progress. Documentation can be found in the docs directory
and at https://penfold.owt.com/st7789py.


Examples
--------

See the examples directory for example programs that run on the LILYGO® TTGO T-Display.

Fonts
-----

See the subdirectories in the fonts directory for the converted font modules
used in the examples. These modules can be compiled using the mpy-cross
compiler before uploading to save memory.
