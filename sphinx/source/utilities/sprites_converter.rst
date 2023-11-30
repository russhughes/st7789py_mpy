.. _sprites_converter:

sprites_converter.py
--------------------
Convert a sprite sheet image to python a module for use with indexed bitmap method. The Sprite sheet
width and height should be a multiple of sprite width and height. There should be no extra pixels
between sprites. All sprites will share the same palette.

.. seealso::
    - :ref:`tiny_toasters.py<tiny_toasters>`.

Example
^^^^^^^

.. code-block:: console

    # create a sprite sheet with 7 colored sprites 32x32 pixels each
    ./make_colorbars_bitmap.py 227 32 3 --png sprites.png

    # convert the sprite sheet to a python module with 7 sprites
    ./sprites_converter.py sprites.png 32 32 4 > sprites.py

.. code-block:: python

    import tft_config
    import sprites
    tft = tft_config.config(1)
    for i in range(sprites.BITMAPS):
        tft.bitmap(sprites, 0, 0, i)

Usage
^^^^^

.. code-block:: console

    usage: sprites_converter.py [-h] image_file sprite_width sprite_height bits_per_pixel

    Convert image file to python module for use with bitmap method.

    positional arguments:
    image_file      Name of file containing image to convert
    sprite_width    Width of sprites in pixels
    sprite_height   Height of sprites in pixels
    bits_per_pixel  The number of bits to use per pixel (1..8)

    optional arguments:
    -h, --help      show this help message and exit

