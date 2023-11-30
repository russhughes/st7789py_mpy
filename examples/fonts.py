"""
fonts.py
========

.. figure:: ../_static/fonts.jpg
    :align: center

    Test text_font_converter.py

Pages through all characters of four fonts on the Display.
https://www.youtube.com/watch?v=2cnAhEucPD4

.. note:: This example requires the following modules:

  .. hlist::
    :columns: 3

    - `st7789py`
    - `tft_config`
    - `vga2_8x8`
    - `vga2_8x16`
    - `vga2_bold_16x16`
    - `vga2_bold_16x32`

"""

import utime
import st7789py as st7789
import tft_config
import vga2_8x8 as font1
import vga2_8x16 as font2
import vga2_bold_16x16 as font3
import vga2_bold_16x32 as font4


def main():
    tft = tft_config.config(tft_config.WIDE)
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
