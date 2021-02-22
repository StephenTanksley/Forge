import teek
import threading
from poe_gui import POEForge
from poe_preset import Preset
from poe_input import Mouse, Keyboard
from pynput import mouse

# # This class will be a wrapper class which manages instances of the Mouse, Keyboard, GUI and the script itself. This globalizes state and manages the dispatch of data between components.


class App:
    def __init__(self):
        self.preset = Preset("something here")
        self.test_mouse = Mouse()
        self.keyboard = Keyboard()

        teek.init_threads()

        # I have to have these lines like this because
        window = teek.Window("Path of Exile Forge")
        window.geometry(800, 600)
        POEForge(window)

        # I'll need a keyboard controller and a mouse controller here eventually.
        # MouseListener = mouse.Listener(
        #     on_move=test_mouse.on_move, on_click=test_mouse.on_click, on_scroll=test_mouse.on_scroll)
        # MouseListener.start()

        window.on_delete_window.connect(teek.quit)
        print("I'm running from the App.")
        teek.run()


App()




# This is where the threads for the program are actually initiated.
