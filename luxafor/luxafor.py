#!/usr/bin/env python3

import usb.core
import usb.util


class Leds(object):
    """
    Helper class with static attributes to select Luxafor leds.

    - All: All the leds.
    - Front: Front side of the flag.
    - Back: Back side of the flag.
    - Led#: Specific led number.

              +--------------------------+
              |    |                     |
              |6  3|                     |
              |    |                     |
    Front side|5  2|Back side            |
              |    |                     |
              |4  1|                     |
              |    |                     |
              |    +---------------------+
              |    |
              |    |
              |    |
              |    |
              +----+
    """
    ALL = 0xFF
    BACK = 0x41
    FRONT = 0x42

    LED1 = 0x01
    LED2 = 0x02
    LED3 = 0x03
    LED4 = 0x04
    LED5 = 0x05
    LED6 = 0x06


class Packet(object):
    byte0 = 0
    byte1 = 0
    byte2 = None
    byte3 = None
    byte4 = None
    byte5 = None
    byte6 = None
    byte7 = None

    def get_byte(self, byte_num):
        return getattr(self, 'byte%d' % byte_num, None)

    def render(self):
        pkt = filter(
            lambda x: x is not None,
            (self.get_byte(n) for n in range(8)))
        return tuple(pkt)


class Luxafor(object):
    VENDOR_ID = 0x04D8
    PRODUCT_ID = 0xF372

    DEVICE_ID = 1

    COLORS = {
        'red': 0x52,
        'green': 0x47,
        'blue': 0x42,
        'cyan': 0x43,
        'magenta': 0x4D,
        'yellow': 0x59,
        'white': 0x57,
        'off': 0x4F,
    }

    def __init__(self):
        device = usb.core.find(idVendor=self.VENDOR_ID,
                               idProduct=self.PRODUCT_ID)

        if device is None:
            raise Exception('Device was not found.')

        try:
            device.set_configuration()
        except usb.core.USBError:
            # Prevent Resource busy errors
            device.detach_kernel_driver(0)
            device.set_configuration()

        self.device = device

    def set_basic_color(self, color):
        if color in self.COLORS:
            pkt = Packet()
            pkt.byte0 = 0
            pkt.byte1 = self.COLORS.get(color, 79)

            self.device.write(self.DEVICE_ID, pkt.render())

    def set_color(self, red=255, green=255, blue=255, led=Leds.ALL):
        pkt = Packet()
        pkt.byte0 = 1
        pkt.byte1 = led
        pkt.byte2 = red
        pkt.byte3 = green
        pkt.byte4 = blue
        self.device.write(self.DEVICE_ID, pkt.render())

    def fade(self, red=255, green=255, blue=255, led=Leds.ALL, speed=255):
        pkt = Packet()
        pkt.byte0 = 2
        pkt.byte1 = led
        pkt.byte2 = red
        pkt.byte3 = green
        pkt.byte4 = blue
        pkt.byte5 = speed
        self.device.write(self.DEVICE_ID, pkt.render())

    def strobe(self, red=255, green=255, blue=255, led=Leds.ALL,
               speed=6, repeat=1):
        pkt = Packet()
        pkt.byte0 = 3
        pkt.byte1 = led
        pkt.byte2 = red
        pkt.byte3 = green
        pkt.byte4 = blue
        pkt.byte5 = speed
        pkt.byte6 = 0
        pkt.byte7 = repeat
        self.device.write(self.DEVICE_ID, pkt.render())

    def wave(self, red=255, green=255, blue=255, wave=1, duration=2, repeat=1):
        pkt = Packet()
        pkt.byte0 = 4
        pkt.byte1 = wave
        pkt.byte2 = red
        pkt.byte3 = green
        pkt.byte4 = blue
        pkt.byte5 = 0
        pkt.byte6 = repeat
        pkt.byte7 = duration
        self.device.write(self.DEVICE_ID, pkt.render())

    def pattern(self, pattern=0, repeat=255):
        pkt = Packet()
        pkt.byte0 = 6
        pkt.byte1 = pattern
        pkt.byte2 = repeat
        self.device.write(self.DEVICE_ID, pkt.render())

    def turn_off(self):
        self.set_basic_color('off')
