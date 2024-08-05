""" ESP32-2432S028R 320x240 st7789 display sometimes known as "Cheap Yellow Board" (CYD) - this is the v3 board

"""

from machine import Pin, SPI
import st7789py as st7789

TFA = 40
BFA = 40
WIDE = 1
TALL = 0
SCROLL = 0      # orientation for scroll.py
FEATHERS = 1    # orientation for feathers.py

def config(rotation=0):
    """
    Configures and returns an instance of the ST7789 display driver.

    Args:
        rotation (int): The rotation of the display (default: 0).

    Returns:
        ST7789: An instance of the ST7789 display driver.
    """

    return st7789.ST7789(
        SPI(1, baudrate=40000000, sck=Pin(14), mosi=Pin(13), miso=None),
        240,
        320,
        reset=Pin(0, Pin.OUT),
        cs=Pin(15, Pin.OUT),
        dc=Pin(2, Pin.OUT),
        backlight=Pin(21, Pin.OUT),
        rotation=rotation)
