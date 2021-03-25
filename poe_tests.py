import unittest
from poe_ui import POEForge
from poe_preset import Preset
from poe_input import Mouse, Keyboard
from event_bus import EventBus
import teek

"""--------- UNIT TESTS ---------"""


class InputUnitTest(unittest.TestCase):

    """
        Tests in this suite will determine whether the input listeners work properly and are getting the proper data that's expected.
    """

    def setUp(self):
        self.bus = EventBus()
        self.mouse = Mouse(self.bus)
        self.keyboard = Keyboard(self.bus)


class PresetUnitTest(unittest.TestCase):

    """
        Tests in this suite will determine if the methods encapsulated in the Preset class properly modify the private attributes of the class.

    """

    def setUp(self):
        self.bus = EventBus()
        self.preset = Preset("test", self.bus, item="helmet",
                             xy_1=(0, 1), xy_2=(1, 2))

    def test_get_name(self):
        self.assertEqual(self.preset.get_name(), "test")

    def test_set_name(self):
        self.preset.set_name("test_1")
        self.assertEqual(self.preset.get_name(), "test_1")

    def test_get_item(self):
        self.assertEqual(self.preset.get_item(), "helmet")

    def test_set_item(self):
        self.preset.set_item("sword")
        self.assertEqual(self.preset.get_item(), "sword")

    def test_get_xy_1(self):
        self.assertEqual(self.preset.get_xy_1(), (0, 1))

    def test_set_xy_1(self):
        self.preset.set_xy_1((99.0, 99.1))
        self.assertEqual(self.preset.get_xy_1(), (99.0, 99.1))

    def test_get_xy_2(self):
        self.assertEqual(self.preset.get_xy_2(), (1, 2))

    def test_set_xy_2(self):
        self.preset.set_xy_2((100.0, 100.1))
        self.assertEqual(self.preset.get_xy_2(), (100.0, 100.1))

    def test_clear_preset(self):
        self.preset.clear_preset()
        self.assertEqual(self.preset.get_name(), None)
        self.assertEqual(self.preset.get_item(), None)
        self.assertEqual(self.preset.get_xy_1(), (0, 0))
        self.assertEqual(self.preset.get_xy_2(), (0, 0))

    # Still unsure how I'll be handling kwargs.


class UIUnitTest(unittest.TestCase):
    """
        Tests in this suite will determine whether the elements of the UI are displaying properly as expected.
    """

    def setUp(self):
        self.bus = EventBus()
        self.window = teek.Window("Testing Window")
        self.window.geometry(800, 600)
        self.ui = POEForge(self.window, self.bus)


"""--------- INTEGRATION TESTS ---------"""


class IntegrationTests(unittest.TestCase):

    """
        I expect this to be the longest test suite. Tests in this suite will determine if data 

    """

    def setUp(self):
        self.bus = EventBus()
        self.window = teek.Window("Testing Window")
        self.window.geometry(800, 600)
        ui = POEForge(self.window, self.bus)

        self.mouse = Mouse(self.bus)
        self.keyboard = Keyboard(self.bus)
        self.preset = Preset("test", self.bus, xy_1=(0, 1), xy_2=(1, 2))


if __name__ == '__main__':
    unittest.main()
