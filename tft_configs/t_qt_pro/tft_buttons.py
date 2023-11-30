"""
LILYGO® T-QT Pro buttons
"""

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
        self.name = "t-qt-pro"
        self.left = Pin(0, Pin.IN)
        self.right = Pin(47, Pin.IN)

        # need more buttons for roids.py
        self.fire = None
        self.thrust = None
        self.hyper = None
