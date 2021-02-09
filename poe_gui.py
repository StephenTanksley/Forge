import teek
import threading
from poe_script import Preset
from poe_input import Mouse
from pynput import mouse


class POEForge(teek.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        preset = Preset("First Preset Object", (0, 0), (0, 0), False)

        description = teek.Label(
            window, "This is a utility for crafting new sexy items in Path of Exile.")
        description.grid(column=0, row=0)

        instructions = teek.Text(window)
        instructions.insert(
            instructions.start, "To craft an item, click on the 'Target (x): ' button, then move to the currency item and left-click.")
        instructions.grid(column=0, row=0)
        instructions.config['background'] = teek.Color('blue')

        targets = teek.Frame(window)
        targets.grid(column=0, row=0)
        targets_label = teek.Label(
            targets, text="Current Targets", font=("Helvetica", 20))
        targets_label.grid(column=0, row=1)

        target1 = teek.Label(targets, text="Target 1: ")
        target1.grid(column=0, row=2)

        target2 = teek.Label(targets, text="Target 2: ")
        target2.grid(column=0, row=3)


teek.init_threads()
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
