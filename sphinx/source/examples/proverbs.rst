.. _proverbs:

proverbs.py
===========

.. figure:: ../_static/proverbs.jpg
    :align: center

    Test for TrueType write_font_converter.

Displays what I hope are chinese proverbs in simplified chinese to test UTF-8 font support.
The fonts were converted from True Type fonts using the
:ref:`write_font_converter.py<write_font_converter>` utility.

.. literalinclude:: ../../../examples/proverbs/make_proverbs_fonts.sh


.. note:: This example requires the following modules:

  .. hlist::
    :columns: 3

    - `st7789py`
    - `tft_config`
    - `proverbs_20`
    - `proverbs_30`

.. literalinclude:: ../../../examples/proverbs/proverbs.py
   :language: python
   :linenos:
   :lines: 1-

