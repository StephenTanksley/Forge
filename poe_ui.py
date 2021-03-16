import teek
import threading
from poe_preset import Preset
from poe_input import Mouse
from pynput import mouse


def print_item():
    print("I'm being activated")


class POEForge(teek.Frame):
    def __init__(self, window, *args, **kwargs):
        super().__init__(window, *args, **kwargs)

        targets = teek.Frame(window)
        targets.grid(column=0, row=0)

        # description_1 = """
        # This is a utility for crafting high stat items in Path of Exile.

        # To begin crafting an item, click on the 'Target (x): ' button, then move to the currency item and left-click.

        # Repeat for the other targets.

        # Set the stat tier and max iterations and then save all preferences in a named preset, then click the run button.

        # If you need to stop execution at any time during the runtime, press the Stop button."""

        # description = teek.Text(targets)
        # description.insert(description.start, description_1)
        # description.end

        # description.grid(column=0, row=0, columnspan=7, sticky='nswe')

        """LABELS"""

        label_font_setting = ('Helvetica', 16)

        # targets = teek.LabelFrame(window, text="Path of Exile Forge")
        # targets.grid(column=0, row=0)

        target1 = teek.Label(targets, text="Target 1 coordinates: ")
        target1.config['font'] = label_font_setting
        target1.grid(column=1, row=2, sticky="W", padx=20, pady=5)

        target2 = teek.Label(targets, text="Target 2 coordinates: ")
        target2.config['font'] = label_font_setting
        target2.grid(column=1, row=3, sticky="W", padx=20, pady=5)

        item_target = teek.Label(targets, text="Target Item coordinates: ")
        item_target.config['font'] = label_font_setting
        item_target.grid(column=1, row=4, sticky="W", padx=20, pady=5)

        stat_tier = teek.Label(targets, text="Minimum Stat Tier: ")
        stat_tier.config['font'] = label_font_setting
        stat_tier.grid(column=1, row=5, sticky="W", padx=20, pady=5)

        max_iterations = teek.Label(targets, text="Max # of iterations: ")
        max_iterations.config['font'] = label_font_setting
        max_iterations.grid(column=1, row=6, sticky="W", padx=20, pady=5)

        target_1_limit = teek.Label(targets, "Target 1 currency limit: ")
        target_1_limit.config['font'] = label_font_setting
        target_1_limit.grid(column=5, row=2, sticky="W", padx=20, pady=5)

        target_2_limit = teek.Label(targets, "Target 2 currency limit: ")
        target_2_limit.config['font'] = label_font_setting

        target_2_limit.grid(column=5, row=3, sticky="W", padx=20, pady=5)

        status_label = teek.Label(targets, text="Program Status Updates:")
        status_label.config['font'] = label_font_setting

        status_label.grid(column=8, row=1, columnspan=2,
                          sticky="WS", pady=5)

        # Cycles
        current_cycle_num = teek.IntVar()
        current_cycle_num.set(0)
        cycle_number_label = teek.Label(targets, "Current Cycle: ")
        cycle_number_label.config['font'] = label_font_setting

        cycle_number_label.grid(
            column=8, row=7, sticky="WS")
        cycle_number_count = teek.Label(targets, text=current_cycle_num.get())
        cycle_number_count.grid(
            column=9, row=7, sticky="WS")

        """VARIABLES"""

        """
        To use variables, you can't just try to manually assign them like you would normally in Python. a = 10 won't work. In the case of a, you'd need to write a.set(new_value) because we're technically using a subclass of TclVariable. We need to use the getter/setter methods to access and modify data stored in each object instance.
        """
        t1_x_var = teek.FloatVar()
        t1_y_var = teek.FloatVar()
        t1_var_tuple = (t1_x_var, t1_y_var)

        t2_x_var = teek.FloatVar()
        t2_y_var = teek.FloatVar()
        t2_var_tuple = (t2_x_var, t2_y_var)

        target_item_x = teek.FloatVar()
        target_item_y = teek.FloatVar()
        target_item_tuple = (target_item_x, target_item_y)

        # I may want to define the defaults inside the Preset class.
        # These presets are more of a data attribute that should be handled elsewhere.
        t1_limit_var = teek.IntVar()
        t1_limit_var.set(5000)
        t2_limit_var = teek.IntVar()
        t2_limit_var.set(5000)

        item_stat_tier = teek.IntVar()
        item_stat_tier.set(1)
        stat_tier_entry = teek.Entry(targets, text=item_stat_tier.get())
        stat_tier_entry.grid(column=2, row=5, sticky="W", pady=5)

        max_iterations = teek.IntVar()
        max_iterations.set(5000)

        """BUTTONS"""

        target_1_set = teek.Button(
            targets, text="Set target 1 (x,y)", width=15, command=print_item)
        target_1_set.grid(column=3, row=2, sticky="W", padx=3)

        target_2_set = teek.Button(
            targets, text="Set target 2 (x,y)", width=15, command=print_item)
        target_2_set.grid(column=3, row=3, sticky="W", padx=3)

        item_target_set = teek.Button(
            targets, text="Set item target (x,y)", width=15, command=print_item)
        item_target_set.grid(column=3, row=4, sticky="W", padx=3)

        """INPUT FIELDS"""
        # Will need to BIND these.
        max_iteration_input = teek.Entry(targets, text=max_iterations.get())
        max_iteration_input.grid(
            column=2, row=6, columnspan=2, sticky="W", padx=3)

        t1_limit_input = teek.Entry(targets, text=t1_limit_var.get())
        t1_limit_input.grid(
            column=6, row=2, sticky="W", padx=3)

        t2_limit_input = teek.Entry(targets, text=t2_limit_var.get())
        t2_limit_input.grid(
            column=6, row=3, sticky="W", padx=3)
