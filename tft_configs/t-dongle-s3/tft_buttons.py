"""esp32 T-Dongle-S3 Buttons
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
        self.name = "t-dongle-s3"
        self.button = Pin(0, Pin.IN)
        self.left = self.button
        self.right = self.button

        # need more buttons for roids.py
        self.fire = None
        self.thrust = None
        self.hyper = None
