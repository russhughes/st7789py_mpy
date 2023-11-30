.. _image_converter:

image_converter.py
------------------
Convert an image file to a python module for use with the bitmap method. Use redirection to save the
output to a file. The image is converted to a bitmap using the number of bits per pixel you specify.
The bitmap is saved as a python module that can be imported and used with the bitmap method.

.. seealso::
    - :ref:`alien.py<alien>`.

Example
^^^^^^^

.. code-block:: console

    ./create_png_examples.py cat.png 4 > cat_bitmap.py

The python file can be imported and displayed with the bitmap method. For example:

.. code-block:: python

    import tft_config
    import cat_bitmap
    tft = tft_config.config(1)
    tft.bitmap(cat_bitmap, 0, 0)

Usage
^^^^^

.. code-block:: console

    usage: image_converter.py [-h] image_file bits_per_pixel

    Convert image file to python module for use with bitmap method.

    positional arguments: image_file      Name of file containing image to convert bits_per_pixel
    The number of bits to use per pixel (1..8)

    optional arguments: -h, --help      show this help message and exit

