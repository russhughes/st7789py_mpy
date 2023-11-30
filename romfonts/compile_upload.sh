#!/bin/sh
mpy-cross vga1_16x16.py
mpy-cross vga1_16x32.py
mpy-cross vga1_8x16.py
mpy-cross vga1_8x8.py
mpy-cross vga1_bold_16x16.py
mpy-cross vga1_bold_16x32.py
mpy-cross vga2_16x16.py
mpy-cross vga2_16x32.py
mpy-cross vga2_8x16.py
mpy-cross vga2_8x8.py
mpy-cross vga2_bold_16x16.py
mpy-cross vga2_bold_16x32.py

cd ..
mpremote cp -r romfonts/*.mpy :
