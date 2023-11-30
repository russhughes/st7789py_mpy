.. _make_colorbars_bitmap:

make_colorbars_bitmap.py
------------------------
Create a MicroPython bitmap module with WHITE, YELLOW, CYAN, GREEN, MAGENTA, RED, and BLUE
color bars for testing. Use redirection to save the output to a file.  The bitmap is saved
as a python module that can be imported and used with the bitmap method.

.. seealso::
  :ref:`colorbars.py<colorbars>`.

Example
^^^^^^^

.. code-block:: console

    ./make_colorbars_bitmap.py 320 240 3 > colorbars_bitmap320x240.py

The python file can be imported and displayed with the bitmap method. For example:

.. code-block:: python

    import tft_config
    import colorbars_bitmap320x240
    tft = tft_config.config(1)
    tft.bitmap(colorbars_bitmap320x240, 0, 0)

Usage
^^^^^

.. code-block:: console

usage: make_colorbars_bitmap.py [-h] [--png png] width height bits_per_pixel

Create a bitmap module with color bars for use with the bitmap method.

positional arguments:
  width           The width of the image in pixels
  height          The height of the image in pixels
  bits_per_pixel  The number of bits to use per pixel (1..8)

optional arguments:
  -h, --help      show this help message and exit
  --png png       Optionally create png file

