"""
M5STACK AtomS3 buttons
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
        self.name = "AtomS3"
        self.left = None
        self.right = None
        self.fire = None
        self.thrust = None
        self.hyper = None
