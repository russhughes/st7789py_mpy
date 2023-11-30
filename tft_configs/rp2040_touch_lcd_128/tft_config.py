"""RP2040-Touch-LCD-1.28 240x240 (GC9A01)
"""

from machine import Pin, SPI
import st7789py as st7789

TFA = 0
BFA = 0
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

    INIT_CMDS = (
        (b"\xEF", None, 0),
        (b"\xEB", b"\x14", 0),
        (b"\xFE", None, 0),
        (b"\xEF", None, 0),
        (b"\xEB", b"\x14", 0),
        (b"\x84", b"\x40", 0),
        (b"\x85", b"\xFF", 0),
        (b"\x86", b"\xFF", 0),
        (b"\x87", b"\xFF", 0),
        (b"\x88", b"\x0A", 0),
        (b"\x89", b"\x21", 0),
        (b"\x8A", b"\x00", 0),
        (b"\x8B", b"\x80", 0),
        (b"\x8C", b"\x01", 0),
        (b"\x8D", b"\x01", 0),
        (b"\x8E", b"\xFF", 0),
        (b"\x8F", b"\xFF", 0),
        (b"\xB6", b"\x00\x00", 0),
        (b"\x3A", b"\x55", 0),
        (b"\x90", b"\x08\x08\x08\x08", 0),
        (b"\xBD", b"\x06", 0),
        (b"\xBC", b"\x00", 0),
        (b"\xFF", b"\x60\x01\x04", 0),
        (b"\xC3", b"\x13", 0),
        (b"\xC4", b"\x13", 0),
        (b"\xC9", b"\x22", 0),
        (b"\xBE", b"\x11", 0),
        (b"\xE1", b"\x10\x0E", 0),
        (b"\xDF", b"\x21\x0c\x02", 0),
        (b"\xF0", b"\x45\x09\x08\x08\x26\x2A", 0),
        (b"\xF1", b"\x43\x70\x72\x36\x37\x6F", 0),
        (b"\xF2", b"\x45\x09\x08\x08\x26\x2A", 0),
        (b"\xF3", b"\x43\x70\x72\x36\x37\x6F", 0),
        (b"\xED", b"\x1B\x0B", 0),
        (b"\xAE", b"\x77", 0),
        (b"\xCD", b"\x63", 0),
        (b"\x70", b"\x07\x07\x04\x0E\x0F\x09\x07\x08\x03", 0),
        (b"\xE8", b"\x34", 0),
        (b"\x62", b"\x18\x0D\x71\xED\x70\x70\x18\x0F\x71\xEF\x70\x70", 0),
        (b"\x63", b"\x18\x11\x71\xF1\x70\x70\x18\x13\x71\xF3\x70\x70", 0),
        (b"\x64", b"\x28\x29\xF1\x01\xF1\x00\x07", 0),
        (b"\x66", b"\x3C\x00\xCD\x67\x45\x45\x10\x00\x00\x00", 0),
        (b"\x67", b"\x00\x3C\x00\x00\x00\x01\x54\x10\x32\x98", 0),
        (b"\x74", b"\x10\x85\x80\x00\x00\x4E\x00", 0),
        (b"\x98", b"\x3e\x07", 0),
        (b"\x35", None, 0),
        (b"\x21", None, 0),
        (b"\x11", None, 120),
        (b"\x29", None, 120),
    )

    DISPLAY_240x240 = (
        (0x48, 240, 240,  0,  0, False),
        (0x28, 240, 240,  0,  0, False),
        (0x88, 240, 240,  0,  0, False),
        (0xe8, 240, 240,  0,  0, False))

    spi = SPI(1, baudrate=60000000, sck=Pin(10), mosi=Pin(11))
    return st7789.ST7789(
        spi,
        240,
        240,
        reset=Pin(13, Pin.OUT),
        cs=Pin(9, Pin.OUT),
        dc=Pin(8, Pin.OUT),
        backlight=Pin(25, Pin.OUT),
        rotation=rotation,
        custom_init=INIT_CMDS,
        custom_rotations=DISPLAY_240x240,
    )
