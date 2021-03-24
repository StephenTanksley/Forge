import unittest
from poe_ui import POEForge
from poe_preset import Preset
from poe_input import Mouse, Keyboard
from event_bus import EventBus
import teek

# Unit Tests
# These will test whether the lights are working.


class InputUnitTest(unittest.TestCase):
    def setUp(self):
        bus = EventBus()
        mouse = Mouse(bus)
        keyboard = Keyboard(bus)


class PresetUnitTest(unittest.TestCase):
    def setUp(self):
        bus = EventBus()
        mouse = Mouse(bus)
        keyboard = Keyboard(bus)
        preset = Preset("test", "test helmet", (0, 1), (1, 2))

        window = teek.Window("Testing Window")
        window.geometry(800, 600)
        ui = POEForge(window, bus)

    def test_preset(self):
        pass

    def test_input(self):
        pass

    def test_ui(self):
        pass


class UIUnitTest(unittest.TestCase):
    pass
    # Integration tests
    # These will test whether systems are integrated properly and passing data where it needs to go.


class IntegrationTests(unittest.TestCase):
    def setUp(self):

        window = teek.Window("Testing Window")
        window.geometry(800, 600)
        ui = POEForge(window)

        mouse = Mouse()
        keyboard = Keyboard()
        preset = Preset("test", "test helmet", (0, 1), (1, 2))
