import unittest
from pynput import mouse, keyboard
from poe_ui import POEForge
from poe_preset import Preset
from poe_data_queue import DataQueue
from poe_input import Mouse, Keyboard
from event_bus import EventBus
import teek

"""------------- UNIT TESTS -------------"""


class InputUnitTest(unittest.TestCase):

    """
        Tests in this suite will determine whether the input listeners work properly and are getting the proper data that's expected.

        So what do I need these unit tests for the inputs to even do?

        I need them to make sure that they're getting the correct data from the mouse.
    """

    def setUp(self):
        self.bus = EventBus()
        self.mouse = Mouse(self.bus)
        self.keyboard = Keyboard(self.bus)

    def tearDown(self):
        self.keyboard = None
        self.mouse = None
        self.bus = None

    """
        Tests in this suite will determine if the methods encapsulated in the Preset class properly modify the private attributes of the class.
    """


class PresetUnitTest(unittest.TestCase):

    def setUp(self):
        self.bus = EventBus()
        self.preset = Preset("test", self.bus, item="helmet",
                             xy_1=(0, 1), xy_2=(1, 2))

    def tearDown(self):
        self.bus = None
        self.preset = None

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


"""
      Tests in this suite will determine if the methods encapsulated in the Preset class properly modify the private attributes of the class.

"""


class DataQueueTest(unittest.TestCase):
    def setUp(self):
        self.dq = DataQueue()

    def tearDown(self):
        self.dq = None

    def test_enqueue(self):
        self.dq.enqueue(1)
        self.assertEqual(self.dq._queue[0], 1)
        self.assertNotEqual(self.dq._queue[0], 0)

    def test_dequeue(self):
        self.dq.enqueue(1)
        integer = self.dq.dequeue()
        self.assertEqual(integer, 1)

    def test_is_empty_false(self):
        self.dq.enqueue(1)
        self.assertFalse(self.dq.is_empty())

    def test_is_empty_true(self):
        self.dq.flush_queue()
        self.assertTrue(self.dq.is_empty())

    def test_view_queue(self):
        self.dq.enqueue(1)
        self.assertEqual(self.dq.view_queue(), [1])

    def test_flush_queue(self):
        self.dq.enqueue(1)
        self.dq.enqueue(2)
        self.dq.flush_queue()
        self.assertEqual(self.dq._queue, [])


class UIUnitTest(unittest.TestCase):
    """
        Tests in this suite will determine whether the elements of the UI are displaying properly as expected.
    """

    def setUp(self):
        self.bus = EventBus()
        self.window = teek.Window("Testing Window")
        self.window.geometry(800, 600)
        self.ui = POEForge(self.window, self.bus)


"""------------- INTEGRATION TESTS -------------"""


class IntegrationTests(unittest.TestCase):

    """
        I expect this to be the longest test suite. Tests in this suite will determine if data is being transported and manipulated in the ways that I want it to be. These tests will take the following form:

        1) Begin test in Preset with expected state data.
        2) Invoke methods to mimic user interaction with the interface.
        3) Create assertions which check the end state of Preset which will be mutated by the operation.
        4) Along the way, check that each link in the chain is returning the required data.
            i.e. 

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
