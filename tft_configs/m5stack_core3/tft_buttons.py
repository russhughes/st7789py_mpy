# M5STACK CORES3
#  - Not working with DUAL BUTTON unit

# DIN Base
#   Port A  1,  2
#   Port B  8,  9
#   Port C 18, 17

from machine import Pin

class Buttons:
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
        self.name = "m5stack_cores3"
        self.left = Pin(1, Pin.IN, Pin.PULL_UP)  # PORT A
        self.right = Pin(2, Pin.IN, Pin.PULL_UP) # PORT A
        self.fire = None
        self.thrust = None
        self.hyper = None
