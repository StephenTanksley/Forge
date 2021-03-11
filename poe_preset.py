
"""
    The SETTING class. Should store coordinates for the first and second items as an (x, y) tuple. 
    
    This class might need some love down the road. Right now I can only capture 
"""


class Preset:
    def __init__(self, name, item=None, xy_0=(0, 0), xy_1=(0, 0), **kwargs):
        self.name = name
        self.item = item
        self.xy_0 = xy_0
        self.xy_1 = xy_1

    def __str__(self):
        return f'\nPreset name: {self.name}\nItem: {self.item}\nFirst coordinate pair: ({self.xy_0})\nSecond coordinate pair: ({self.xy_1})\n'

    def __repr__(self):
        return f'[{self.name}, {self.xy_0}, {self.xy_1}]'

    def change_target(self, target, x, y):
        if target == 0:
            self.xy_0 = (x, y)
        elif target == 1:
            self.xy_1 = (x, y)


# https://github.com/seanpar203/event-bus - Creates a publish/subscribe model for events. This is what I need to be using to get the data from various events going in the right directions.
