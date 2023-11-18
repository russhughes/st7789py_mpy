Python ST7789 driver for MicroPython
====================================

This is a fork of devbis' st7789py_mpy module from
https://github.com/devbis/st7789py_mpy.

This driver has support for:

- 320x240, 240x240, 135x240, and 128x128 pixel displays
- RGB and BGR Color Orders
- Display rotation
- Hardware based scrolling
- Drawing text using converted PC BIOS bitmap fonts
- Drawing text using converted TrueType fonts.
- Drawing converted bitmaps

This is a work in progress. Documentation can be found in the docs directory
and at https://penfold.owt.com/st7789py.


Examples
--------

See the examples directory for example programs that run on:

- M5STACK AtomS3
- Generic ESP32 connected to a 320x240 display
- LILYGO® TTGO T-Display
- LILYGO® TTGO T-Display RP2040
- Raspberry Pi Pico
  - Waveshare 1.3"
  - Waveshare 1.14"

Fonts
-----

See the subdirectories in the fonts directory for the converted font modules
used in the examples. These modules can be compiled using the mpy-cross
compiler before uploading to save memory.


