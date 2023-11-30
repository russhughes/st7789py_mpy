"""
Waveshare 1.3" TFT display with ST7789 controller
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
        self.name = "waveshare_13"
        self.left = Pin(16, Pin.IN, Pin.PULL_UP) # Joystick left
        self.right = Pin(20, Pin.IN, Pin.PULL_UP) # Joystick right
        self.fire = Pin(21, Pin.IN, Pin.PULL_UP) # Joystick press
        self.thrust = Pin(3, Pin.IN, Pin.PULL_UP) # Y button
        self.hyper = Pin(15, Pin.IN, Pin.PULL_UP) # A button
