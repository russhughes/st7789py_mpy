****************
Example Programs
****************

320x240 Example Programs
========================

These examples run on a ESP32 board with a 320x240 display. They are were tested using a SparkFun
ESP32 Thing and a Waveshare 2 inch LCD ST7789 Module.  You may need to modify the pin use for your
device.

320x240 lines.py
----------------

.. literalinclude:: ../../examples/esp32_320x240/lines.py
   :linenos:
   :language: python


320x240  hello.py
-----------------

.. literalinclude:: ../../examples/esp32_320x240/hello.py
   :linenos:
   :language: python


320x240 feathers.py
-------------------

.. literalinclude:: ../../examples/esp32_320x240/feathers.py
   :linenos:
   :language: python

320x240 fonts.py
----------------

.. literalinclude:: ../../examples/esp32_320x240/fonts.py
   :linenos:
   :language: python



320x240 scroll.py
-----------------

.. literalinclude:: ../../examples/esp32_320x240/scroll.py
   :linenos:
   :language: python


320x240 toasters.py
-------------------

Flying toasters sprite demo using bitmaps created from spritesheet using the sprites2bitmap.py
utility. See the maketoast shell script for the command line used to create the toast_bitmaps.py from the
toasters.bmp image.

.. literalinclude:: ../../examples/esp32_320x240/toasters/toasters.py
   :linenos:
   :language: python


135x240 TTGO T-Display Example Programs
=======================================

These examples run on the LilyGo TTGO-T-Display available from the usual
locations. See https://github.com/Xinyuan-LilyGO/TTGO-T-Display for more
information.


lines.py
--------

.. literalinclude:: ../../examples/ttgo_tdisplay/lines.py
   :linenos:
   :language: python


hello.py
--------

.. literalinclude:: ../../examples/ttgo_tdisplay/hello.py
   :linenos:
   :language: python

feathers.py
-----------

.. literalinclude:: ../../examples/ttgo_tdisplay/feathers.py
   :linenos:
   :language: python


fonts.py
--------

.. literalinclude:: ../../examples/ttgo_tdisplay/fonts.py
   :linenos:
   :language: python


scroll.py
---------

.. literalinclude:: ../../examples/ttgo_tdisplay/scroll.py
   :linenos:
   :language: python


toasters.py
-----------

Flying toasters sprite demo using bitmaps created from spritesheet using the imgtobitmap.py utility.
See the maketoast script in the utils directory for details.  See the 320x240 toasters example for
a more advanced example that uses the sprites2bitmap utility and indexed bitmaps.

.. literalinclude:: ../../examples/ttgo_tdisplay/toasters/toasters.py
   :linenos:
   :language: python


chango.py
---------

Test for font2bitmap converter for the driver.
See the font2bitmap program in the utils directory.

.. literalinclude:: ../../examples/ttgo_tdisplay/truetype/chango.py
   :linenos:
   :language: python


noto_fonts.py
-------------

Test for font2bitmap converter for the driver.
See the font2bitmap program in the utils directory.

.. literalinclude:: ../../examples/ttgo_tdisplay/truetype/noto_fonts.py
   :linenos:
   :language: python

