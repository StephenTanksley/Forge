import teek
import threading
from poe_preset import Preset
from poe_input import Mouse
from pynput import mouse


class POEForge(teek.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        description = teek.Text(window)
        print(description.end)
        # description.insert()

        # , "This is a utility for crafting high stat items in Path of Exile. \nTo begin crafting an item, click on the 'Target (x): ' button, then move to the currency item and left-click. \nRepeat for the other targets. Set the stat tier and max iterations and then save all preferences in a named preset. Then click the run button. If you need to stop execution at any time during the runtime, press the Stop button."

        description.grid(column=0, row=0)

        # Creating a frame for targets.
        targets = teek.LabelFrame(window, text="Targets")
        targets.grid(column=1, row=1)

        target1 = teek.Label(targets, text="Target 1: ")
        target1.grid(column=1, row=2)

        target2 = teek.Label(targets, text="Target 2: ")
        target2.grid(column=1, row=3)


# This is where the threads for the program are actually initiated.
teek.init_threads()

# I have to have these lines like this because
window = teek.Window("Path of Exile Forge")
POEForge(window)
window.geometry(800, 600)

test_mouse = Mouse()

# I'll need a keyboard controller and a mouse controller here eventually.
MouseListener = mouse.Listener(
    on_move=test_mouse.on_move, on_click=test_mouse.on_click, on_scroll=test_mouse.on_scroll)
MouseListener.start()

window.on_delete_window.connect(teek.quit)
teek.run()
