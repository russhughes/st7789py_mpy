2023-11-29
----------

  - Changed examples to use the same source code, with different
    `tft_config.py` and `tft_buttons.py` modules. This is to make it easier to support additional devices and configurations.
  - Added `tft_buttons.py` modules to support the buttons.
  - Added `tft_config.py` modules to support different configurations.
  - Added examples to demonstrate and test new features.
  - Changed `text()` method to user micropython.viper to improve performance.
  - Added `polygon()` method to draw polygons with optional rotation. This is not fast, but it works.
  - Added `make-example.py` script to generate documentation for examples, configs and utilities.
  - Added documentation for examples, configs and utilities extracted from docstrings using `make-example.py`.
  - Added color_order parameter to st7789py to allow different color orders.
  - Added custom_init parameter to st7789py to allow custom initialization of the display.
  - Added custom_rotation parameter to st7789py to allow custom display sizes, rotations and byte swapping for color data.
  - Added `pbitmap` method to support drawing bitmap graphics one line at a time.
  - Added `examples/upload_all.sh` script to upload all examples to the board.
  - Added `run_all.sh` script to run all examples on the board.
  - Updated and improved documentation.
