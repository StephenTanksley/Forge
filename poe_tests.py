import unittest
from poe_gui import POEForge
from poe_preset import Preset
from poe_input import Mouse, Keyboard
import teek


class InterfaceTest(unittest.TestCase):
    def setUp(self):

        window = teek.Window("Testing Window")
        window.geometry(800, 600)
        ui = POEForge(window)

        mouse = Mouse()
        keyboard = Keyboard()
        preset = Preset("test")

    def test_preset(self):

        pass

    def test_input(self):
        pass

    def test_ui(self):
        pass
