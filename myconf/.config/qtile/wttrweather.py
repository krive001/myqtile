# -*- coding: utf-8 -*-
# Copyright (C) 2019, Krisztián Veress <krive001@gmail.com>


import requests
import subprocess
from libqtile.widget import base
# from libqtile.widget import groupbox

# __all__ = ['WttrWeather']


class WttrWeather(base.ThreadedPollText):
    """Display https://wttr.in weather."""

    orientations = base.ORIENTATION_HORIZONTAL
    defaults = [
        ('location', 'London', 'Add location'),
        ('units', '&m', '&u USCS &m metric and &M  speed in m/s'),
        ('format', '2', '1-4 change variable'),
        ('execute', None, 'Command to execute on click'),
    ]

    def __init__(self, **config):
        base.ThreadedPollText.__init__(self, **config)
        self.add_defaults(WttrWeather.defaults)

    def poll(self):
        url = ('https://wttr.in/' + self.location +
               '?format=' + self.format + self.units)
        data = requests.get(url, headers={'user-agent': 'curl'})

        if data.ok is False:
            output = "N/A"
        else:
            output = data.text
        return output.strip('\n')

    def button_press(self, x, y, button):
        base.ThreadedPollText.button_press(self, x, y, button)
        if button == 1 and self.execute is not None:
            subprocess.Popen([self.execute], shell=True)
