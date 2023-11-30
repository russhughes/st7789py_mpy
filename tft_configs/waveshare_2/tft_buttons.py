"""
input pins for ws_pico_2
"""

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
        self.name = "ws_pico_2"
        self.key0 = Pin(15, Pin.IN, Pin.PULL_UP)    # Top Right
        self.key1 = Pin(17, Pin.IN, Pin.PULL_UP)    # Bottom Right
        self.key2 = Pin(2, Pin.IN, Pin.PULL_UP)     # Bottom Left
        self.key3 = Pin(3, Pin.IN, Pin.PULL_UP)     # Top Left

        # for roids.py in landscape mode

        self.left = self.key2
        self.right = self.key3
        self.fire = self.key1
        self.thrust = self.key0
        self.hyper = None
