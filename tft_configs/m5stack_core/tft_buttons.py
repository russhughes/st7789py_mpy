
# input pins for ws_pico_13

from machine import Pin


class Buttons():
    """
    Buttons class for examples, modify for your device.

    Attributes:
        name (str): The name of the device.
        left (Pin): The Pin object representing the left button.
        right (Pin): The Pin object representing the right button.
        fire (Pin): The Pin object representing the fire button.
        thrust (Pin): The Pin object representing the thrust button.
        hyper (Pin): The Pin object representing the hyper button.
    """

    def __init__(self):
        self.name = "m5stack_core"

        self.left = Pin(39, Pin.IN)  # button A
        self.fire = Pin(38, Pin.IN)  # button B
        self.right = Pin(37, Pin.IN)  # button C
        self.thrust = None
        self.hyper = None
