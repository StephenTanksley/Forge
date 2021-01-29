from pynput.mouse import Button, Controller
from pynput import mouse, keyboard

# Algorithms and code up here


"""
    The SETTING class. Should store coordinates for the first and second items as an (x, y) tuple. The 
"""


class Preset:
    def __init__(self, name, xy_0=(0, 0), xy_1=(0, 0), active=False):
        self.name = name
        self.xy_0 = xy_0
        self.xy_1 = xy_1
        self.active = active

    def __str__(self):
        return f'\nPreset name: {self.name}\nFirst coordinate pair: ({self.xy_0})\nSecond coordinate pair: ({self.xy_1})\nCurrently Active: {self.active}\n'

    def __repr__(self):
        return f'[{self.xy_0}, {self.xy_1}, {self.active}]'

    def change_target(self, target, x, y):
        if target == 0:
            self.xy_0 = (x, y)
        elif target == 1:
            self.xy_1 = (x, y)

    def toggle_active(self):
        self.active = True if (self.active == False) else False


preset = Preset("Boots of groovening")

# print(preset.__str__())
print(preset)
