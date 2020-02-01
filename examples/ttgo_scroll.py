"""
ttgo_fonts.py

    Smoothly scrolls numbers up the screen on the LILYGO® TTGO T-Display
    Only works with fonts with heights that are even multiples of the
    screen height, 8 or 16 pixel high.

"""
import utime
import random
from machine import Pin, SPI
import st7789py as st7789

# choose a font

# import vga1_8x8 as font
# import vga2_8x8 as font
# import vga1_8x16 as font
# import vga2_8x16 as font
# import vga1_16x16 as font
# import vga1_bold_16x16 as font
# import vga2_16x16 as font
import vga2_bold_16x16 as font

def main():
    tft = st7789.ST7789(
        SPI(2, baudrate=30000000, polarity=1, phase=1, sck=Pin(18), mosi=Pin(19)),
        135,
        240,
        reset=Pin(23, Pin.OUT),
        cs=Pin(5, Pin.OUT),
        dc=Pin(16, Pin.OUT),
        backlight=Pin(4, Pin.OUT),
        rotation=0)

    last_line = tft.height - font.HEIGHT
    tfa = 40
    tfb = 40
    tft.vscrdef(tfa, 240, tfb)

    tft.fill(st7789.BLUE)
    scroll = 0
    counter = 0
    while True:
        tft.fill_rect(0,scroll, tft.width, 1, st7789.BLUE)

        if scroll % font.HEIGHT == 0:
            counter += 1
            tft.text(
                font,
                str(counter),
                0,
                (scroll + last_line) % tft.height,
                st7789.WHITE,
                st7789.BLUE)

        tft.vscsad(scroll+tfa)
        scroll +=1

        if scroll == tft.height:
            scroll = 0

        utime.sleep(0.005)

main()
