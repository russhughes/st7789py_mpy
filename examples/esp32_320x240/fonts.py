"""
fonts.py

    Pages through all characters of four fonts on the display.

"""
import utime
from machine import Pin, SPI
import st7789py as st7789

# Choose fonts

# from romfonts import vga1_8x8 as font
from romfonts import vga2_8x8 as font1
# from romfonts import vga1_8x16 as font
from romfonts import vga2_8x16 as font2
# from romfonts import vga1_16x16 as font
# from romfonts import vga1_bold_16x16 as font
# from romfonts import vga2_16x16 as font
from romfonts import vga2_bold_16x16 as font3
# from romfonts import vga1_16x32 as font
# from romfonts import vga1_bold_16x32 as font
# from romfonts import vga2_16x32 as font
from romfonts import vga2_bold_16x32 as font4


def main():
    spi = SPI(1, baudrate=31250000, sck=Pin(18), mosi=Pin(19))

    tft = st7789.ST7789(
        spi,
        320,
        240,
        reset=Pin(4, Pin.OUT),
        cs=Pin(13, Pin.OUT),
        dc=Pin(12, Pin.OUT),
        backlight=Pin(15, Pin.OUT),
        rotation=0)

    tft.vscrdef(40, 240, 40)

    while True:
        for font in (font1, font2, font3, font4):
            tft.fill(st7789.BLUE)
            line = 0
            col = 0

            for char in range(font.FIRST, font.LAST):
                tft.text(font, chr(char), col, line, st7789.WHITE, st7789.BLUE)
                col += font.WIDTH
                if col > tft.width - font.WIDTH:
                    col = 0
                    line += font.HEIGHT

                    if line > tft.height-font.HEIGHT:
                        utime.sleep(3)
                        tft.fill(st7789.BLUE)
                        line = 0
                        col = 0

            utime.sleep(3)


main()
