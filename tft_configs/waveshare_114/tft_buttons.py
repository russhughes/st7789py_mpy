"""
Waveshare Pico LCD 1.14 Buttons
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
        self.name = "waveshare_114"
        self.left = Pin(17, Pin.IN)
        self.right = Pin(3, Pin.IN)
        self.fire = Pin(15, Pin.IN)
        self.thrust = Pin(2, Pin.IN)
        self.hyper = None
