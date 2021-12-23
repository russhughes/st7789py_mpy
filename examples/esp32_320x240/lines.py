"""
lines.py

    Draws lines and rectangles in random colors at random locations on the
    display.

"""
import random
from machine import Pin, SPI
import st7789py as st7789


def main():
    # configure display

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

    tft.fill(st7789.BLUE)

    while True:
        tft.line(
            random.randint(0, tft.width),
            random.randint(0, tft.height),
            random.randint(0, tft.width),
            random.randint(0, tft.height),
            st7789.color565(
                random.getrandbits(8),
                random.getrandbits(8),
                random.getrandbits(8)
                )
            )

        width = random.randint(0, tft.width // 2)
        height = random.randint(0, tft.height // 2)
        col = random.randint(0, tft.width - width)
        row = random.randint(0, tft.height - height)
        tft.fill_rect(
            col,
            row,
            width,
            height,
            st7789.color565(
                random.getrandbits(8),
                random.getrandbits(8),
                random.getrandbits(8)
            )
        )


main()
