
"""
    The SETTING class. Should store coordinates for the first and second items as an (x, y) tuple. 
    
    This class might need some love down the road. Right now I can only capture 
"""


class Preset:
    def __init__(self, name, bus, item=None, xy_1=(0, 0), xy_2=(0, 0), active=False, **kwargs):
        self.name = name
        self._bus = bus
        self.item = item
        self.xy_1 = xy_1
        self.xy_2 = xy_2
        self.kwargs = [kwargs]

    def __str__(self):
        return f'\nPreset name: {self.name}\nItem: {self.item}\nFirst coordinate pair: ({self.xy_1})\nSecond coordinate pair: ({self.xy_2})\n'

    def __repr__(self):
        return f'[{self.name}, {self.item}, {self.xy_1}, {self.xy_2}]'

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_item(self):
        return self.item

    def set_item(self, item):
        self.item = item

    def get_xy_1(self):
        return self.xy_1

    def set_xy_1(self, xy_1):
        self.xy_1 = xy_1

    def get_xy_2(self):
        return self.xy_2

    def set_xy_2(self, xy_2):
        self.xy_2 = xy_2

    def clear_preset(self):
        self.set_name(None)
        self.set_item(None)
        self.set_xy_1((0, 0))
        self.set_xy_2((0, 0))


# https://github.com/seanpar203/event-bus - Creates a publish/subscribe model for events. This is what I need to be using to get the data from various events going in the right directions.
