import teek
import threading
from poe_ui import POEForge
from poe_preset import Preset
from poe_input import Mouse, Keyboard
from pynput import mouse, keyboard
from event_bus import EventBus

# # This class will be a wrapper class which manages instances of the Mouse, Keyboard, GUI and the script itself. This globalizes state and manages the dispatch of data between components.

# Look into Python's graph frame
# DGraph - take a look at the startup here. Get to know a bit more of their graph methodology.

# art.smith@centricconsulting.com


# Consider using Docker and RabbitMQ. RabbitMQ would replace my current instances of the event bus. It's only concerned with sending messages between components. Docker would be used to implement instances of my listeners in lightweight Linux containers.


class App:
    def __init__(self):
        self._bus = EventBus()
        self.preset = Preset("something here", self._bus)
        self.controller_mouse = Mouse(self._bus)
        self.controller_keyboard = Keyboard(self._bus)
        self.active = False

        # Possibly a new class? Set up the listener as an object which can be destroyed when no longer needed.

        ClickListener = mouse.Listener(
            on_click=self.controller_mouse.on_click)

        @self._bus.on('click listener')
        def click_listener():
            ClickListener.start()

        @self._bus.on('stop listener')
        def stop_listener():
            ClickListener.stop()

        # spin up threads for Teek
        teek.init_threads()

        window = teek.Window("Path of Exile Forge")
        window.geometry(1280, 720)
        POEForge(window, self._bus)

        window.on_delete_window.connect(teek.quit)
        teek.run()


App()
