"""
scroll.py

    Smoothly scrolls all font characters up the screen on the LILYGO® TTGO
    T-Display. Only works with fonts with heights that are even multiples of
    the screen height, (i.e. 8 or 16 pixels high)

"""
import time
import random
from machine import Pin, SPI
import st7789py as st7789

# choose a font

# from romfonts import vga1_8x8 as font
# from romfonts import vga2_8x8 as font
# from romfonts import vga1_8x16 as font
# from romfonts import vga2_8x16 as font
# from romfonts import vga1_16x16 as font
# from romfonts import vga1_bold_16x16 as font
# from romfonts import vga2_16x16 as font
from romfonts import vga2_bold_16x16 as font


def main():
    spi = SPI(2, baudrate=40000000, sck=Pin(17), mosi=Pin(21), miso=None)
    tft = st7789.ST7789(
        spi,
        128,
        128,
        reset=Pin(34, Pin.OUT),
        cs=Pin(15, Pin.OUT),
        dc=Pin(33, Pin.OUT),
        backlight=Pin(16, Pin.OUT),
        rotation=0,
        color_order=st7789.BGR)

    last_line = tft.height - font.HEIGHT
    tfa = 1                     # top free area when scrolling
    bfa = 3         	        # bottom free area when scrolling

    tft.vscrdef(tfa, tft.height, bfa)

    tft.fill(st7789.BLUE)
    scroll = 0
    character = 0
    while True:
        tft.fill_rect(0, scroll, tft.width, 1, st7789.BLUE)

        if scroll % font.HEIGHT == 0:
            tft.text(
                font,
                f' x{character:02x}= {chr(character)} ',
                0,
                (scroll + last_line) % tft.height,
                st7789.WHITE,
                st7789.BLUE)

            character = (character + 1) % (font.LAST+1)

        tft.vscsad(scroll + tfa)
        scroll += 1
        time.sleep_ms(10)

        if scroll == tft.height:
            scroll = 0


main()
