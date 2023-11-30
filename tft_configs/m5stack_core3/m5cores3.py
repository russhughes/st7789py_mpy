"""
M5CoreS3:
    Very basic class to configure the M5CORES3 power management IC and
    the AW9523 GPIO expander.
"""

from machine import I2C, Pin
from micropython import const

_AXP2101_ADDR = const(0x34)
_AXP2101_CHGLED_SET_CTRL = const(0x69)
_AXP2101_LDO_ONOFF_CTRL0 = const(0x90)
_AXP2101_ALDO1_VOLTAGE = const(0x92)
_AXP2101_ALDO2_VOLTAGE = const(0x93)
_AXP2101_ALDO3_VOLTAGE = const(0x94)
_AXP2101_ALDO4_VOLTAGE = const(0x95)
_AXP2101_DLDO1_VOLTAGE = const(0x99)

_AXP2101_ALDO_1V8 = const(12)
_AXP2101_ALDO_3V3 = const(28)

_AW9523_ADDR = const(0x58)
_AW9523_OUTPUT_PORT0 = const(0x02)
_AW9523_OUTPUT_PORT1 = const(0x03)
_AW9523_CONFIG_PORT0 = const(0x04)
_AW9523_CONFIG_PORT1 = const(0x05)
_AW9523_CTL = const(0x11)
_AW9523_LED_MODE_SWITCH0 = const(0x12)
_AW9523_LED_MODE_SWITCH1 = const(0x13)

# AW9523 Port usage
# Port 0:                           Port 1:
# ==========================        ==========================
# # NODE         LEVEL   DIR        # NODE         LEVEL   DIR
# ==========================        ==========================
# 0 TOUCH_RST    on      OUT	    0 CAM_RST      on      OUT
# 1 BUS_OUT_EN   off     OUT	    1 LCD_RST      on      OUT
# 2 AW_RST       on      OUT	    2 TOUCH_INT    off     IN
# 3 ES_INT       off     IN	        3 AW_INT       off     IN
# 4 TF_SW        off     IN	        4 N/C          off     OUT
# 5 USB_OTG_EN   off     OUT	    5 N/C          off     OUT
# 6 N/C          off     OUT	    6 N/C          off     OUT
# 7 N/C          off     OUT	    7 BOOST_EN     off     OUT

_M5CORE3_TOUCH_RST = const(1)
_M5CORE3_BUS_OUT_EN = const(2)
_M5CORE3_AW_RST = const(4)
_M5CORE3_ES_INT = const(8)
_M5CORE3_TF_SW = const(16)
_M5CORE3_USB_OTG_EN = const(32)
_M5CORE3_CAM_RST = const(1)
_M5CORE3_LCD_RST = const(2)
_M5CORE3_TOUCH_INT = const(4)
_M5CORE3_AW_INT = const(8)
_M5CORE3_BOOST_EN = const(128)


class M5CoreS3:
    """
    M5CoreS3 Class
    """

    def __init__(self):

        self.i2c_sys_bus = I2C(1, scl=Pin(11), sda=Pin(12), freq=100_000)

        # ALDO2 set to 3.3v VDDA_3V3 for ES7210 4 Channel Audio in
        self.i2c_sys_bus.writeto_mem(
            _AXP2101_ADDR, _AXP2101_ALDO2_VOLTAGE, bytes([_AXP2101_ALDO_3V3])
        )

        # ALDO1 set to 1.8v VDD_1V8 for AW88298 Audio out
        self.i2c_sys_bus.writeto_mem(
            _AXP2101_ADDR, _AXP2101_ALDO1_VOLTAGE, bytes([_AXP2101_ALDO_1V8])
        )

        # ALDO3 set to 3.3v VDDCAM_3V3 for Camera Power Supply
        self.i2c_sys_bus.writeto_mem(
            _AXP2101_ADDR, _AXP2101_ALDO3_VOLTAGE, bytes([_AXP2101_ALDO_3V3])
        )

        # ALDO4 set to 3.3v VDD_3V3_SD for SD Card Power Supply
        self.i2c_sys_bus.writeto_mem(
            _AXP2101_ADDR, _AXP2101_ALDO4_VOLTAGE, bytes([_AXP2101_ALDO_3V3])
        )

        # DLDO1 set to 3.3v VDD_BL for Display Backlight
        self.i2c_sys_bus.writeto_mem(
            _AXP2101_ADDR, _AXP2101_DLDO1_VOLTAGE, bytes([_AXP2101_ALDO_3V3])
        )

        # AXP configure CHG_LED
        self.i2c_sys_bus.writeto_mem(
            _AXP2101_ADDR, _AXP2101_CHGLED_SET_CTRL, bytes([0b00110101])
        )

        # AXP enable ALDO~4,BLDO0~2,DIDO1
        self.i2c_sys_bus.writeto_mem(
            _AXP2101_ADDR, _AXP2101_LDO_ONOFF_CTRL0, bytes([0b10111111]))

        # Config_Port0 set ES_INT, TF_SW to INPUT
        self.i2c_sys_bus.writeto_mem(
            _AW9523_ADDR, _AW9523_CONFIG_PORT0, bytes([0b00011000]))

        # Config_Port1 set TOUCH_INT, AW_INT to INPUT
        self.i2c_sys_bus.writeto_mem(
            _AW9523_ADDR, _AW9523_CONFIG_PORT1, bytes([0b00001100]))

        # LED Mode Switch - set GPIO mode.
        self.i2c_sys_bus.writeto_mem(
            _AW9523_ADDR, _AW9523_LED_MODE_SWITCH0, bytes([0b11111111]))

        # LED Mode Switch - set GPIO mode.
        self.i2c_sys_bus.writeto_mem(
            _AW9523_ADDR, _AW9523_LED_MODE_SWITCH1, bytes([0b11111111]))

        # CTL - set Push-Pull mode.
        self.i2c_sys_bus.writeto_mem(
            _AW9523_ADDR, _AW9523_CTL, bytes([0b00010000]))

        # Output_Port0 set TOUCH_RST, AW_RST HIGH
        self.i2c_sys_bus.writeto_mem(
            _AW9523_ADDR, _AW9523_OUTPUT_PORT0, bytes([0b00000101]))

        # Output_Port1 set CAM_RST, LCD_RST  HIGH
        self.i2c_sys_bus.writeto_mem(
            _AW9523_ADDR, _AW9523_OUTPUT_PORT1, bytes([0b00000011]))

M5 = M5CoreS3()
