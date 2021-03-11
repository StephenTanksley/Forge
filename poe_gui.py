import teek
import threading
from poe_preset import Preset
from poe_input import Mouse
from pynput import mouse


class POEForge(teek.Frame):
    def __init__(self, window, *args, **kwargs):
        super().__init__(window, *args, **kwargs)

        # top_frame = teek.Frame(window)
        # description_1 = "This is a utility for crafting high stat items in Path of Exile. To begin crafting an item, click on the 'Target (x): ' button, then move to the currency item and left-click. Repeat for the other targets. Set the stat tier and max iterations and then save all preferences in a named preset. Then click the run button. If you need to stop execution at any time during the runtime, press the Stop button."

        # description = teek.Text(top_frame)
        # description.insert(description.start, description_1)
        # description.end

        # description.grid(column=0, row=0, sticky='nswe')
        # description.pack(fill='x')

        """LABELS"""
        targets = teek.Frame(window)
        targets.grid(column=1, row=1)

        target1 = teek.Label(targets, text="Target 1: ")
        target1.grid(column=1, row=2)

        target2 = teek.Label(targets, text="Target 2: ")
        target2.grid(column=1, row=3)

        item_target = teek.Label(targets, text="Item Target: ")
        item_target.grid(column=1, row=4)

        stat_tier = teek.Label(targets, text="Desired Stat Tier: ")
        stat_tier.grid(column=1, row=5)

        max_iterations = teek.Label(targets, text="Max # of iterations: ")
        max_iterations.grid(column=1, row=6)

        target_1_limit = teek.Label(targets, "Target 1 currency limit: ")
        target_1_limit.grid(column=6, row=2)

        target_2_limit = teek.Label(targets, "Target 2 currency limit: ")
        target_2_limit.grid(column=6, row=3)

        """VARIABLES"""

        """
        To use variables, you can't just try to manually assign them like you would normally in Python. a = 10 won't work. In the case of a, you'd need to write a.set(new_value) because we're technically using a subclass of TclVariable. We need to use the getter/setter methods to access and modify data stored in each object instance.
        """
        t1_x_var = teek.FloatVar()
        t1_y_var = teek.FloatVar()

        t2_x_var = teek.FloatVar()
        t2_y_var = teek.FloatVar()

        t1_limit_var = teek.IntVar()
        t2_limit_var = teek.IntVar()

        """BUTTONS"""

        """INPUT FIELDS"""
