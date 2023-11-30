.. _colorbars:

.. _colorbars.py:

colorbars.py
=============

.. figure:: ../_static/colorbars.jpg
    :align: center

    Test bitmap colors.

Displays WHITE, YELLOW, CYAN, GREEN, MAGENTA, RED, and BLUE color bar bitmap named
colorbars_{WIDTH}x(HEIGHT) on the display. Custom sized bitmap modules can be created
using the :ref:`make_colorbars_bitmap.py<make_colorbars_bitmap>` utility.

.. note:: This example requires the following modules:

  .. hlist::
    :columns: 3

    - `st7789py`
    - `tft_config`
    - `colorbars_{WIDTH}x{HEIGHT}`

.. literalinclude:: ../../../examples/colorbars/colorbars.py
   :language: python
   :linenos:
   :lines: 1-

