import unittest
from poe_gui import POEForge
from poe_preset import Preset
from poe_input import Mouse, Keyboard
import teek


class InterfaceTest(unittest.TestCase):
    def setUp(self):

        window = teek.Window("Testing Window")
        window.geometry(800, 600)
        gui = POEForge(window)

        mouse = Mouse()
        keyboard = Keyboard()
        preset = Preset("test")
