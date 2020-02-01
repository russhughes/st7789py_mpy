st7789.py
=========

This is a fork of devbis' st7789py_mpy module from
https://github.com/devbis/st7789py_mpy.

I modified the original driver for one of my projects by adding support for
display rotation, scrolling and drawing text using 8 and 16 bit wide bitmap
fonts with heights that are multiples of 8.  Included are 12 bitmap fonts
derived from classic pc text mode fonts and a couple of example
programs that run on the TTGO T-Display.

This is a work in progress. More documentation can be found at
https://penfold.owt.com/st7789py/ and videos of the example programs running 
can be seen at https://www.youtube.com/watch?v=atBa0BYPAAc and 
https://www.youtube.com/watch?v=2cnAhEucPD4.

Slow ST7789 driver for MicroPython
==================================

This is a slow MicroPython driver for 240x240 ST7789 display without CS pin
from Ali Express. It also supports 135x240 TTGO Display



Version: 0.1.4

The performance is quite low due to python function call overhead.
If you have a chance to build firmware and you are using
ESP8266/ESP32 controllers, you should try the fast driver
https://github.com/devbis/st7789_mpy

Examples
--------

    # ESP8266
    import machine
    import st7789py
    spi = machine.SPI(1, baudrate=40000000, polarity=1)
    display = st7789py.ST7789(spi, 240, 240, reset=machine.Pin(5, machine.Pin.OUT), dc=machine.Pin(4, machine.Pin.OUT))
    display.init()
    display.pixel(120, 120, st7789py.YELLOW)

