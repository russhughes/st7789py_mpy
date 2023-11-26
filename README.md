Excelent micropython driver for st7789 module forked from:
https://github.com/russhughes/st7789py_mpy

Started this because:

   1 - My lack of experience to compile and develop fast modules in C for use in micropython
   
   2 - Buy a I8080 (parallel 8 bits bus board) to try and learn.

Results:
  Fast micropython only driver for st7789 with 8 bit parallel bus, thanks to what i have learn with (https://github.com/HughMaingauche/ILI9341-parallel-TFT-driver-for-micropython).
  
  Obs.: For ESP32 ONLY!!!!!!!

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


