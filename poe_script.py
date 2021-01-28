from pynput.mouse import Button, Controller
from pynput import mouse, keyboard

# Algorithms and code up here


"""
    The SETTING class. Should store coordinates for the first and second items as an (x, y) tuple. The 
"""


class Preset:
    def __init__(self, xy_0=(0, 0), xy_1=(0, 0), active=False):
        self.xy_0 = xy_0
        self.xy_1 = xy_1
        self.active = active

    def __str__(self):
        return f'First coordinate pair: ({self.xy_0})\nSecond coordinate pair: ({self.xy_1})\nCurrently Active: {self.active}'

    def __repr__(self):
        return f'[{self.xy_0}, {self.xy_1}, {self.active}]'

    def change_target(self, target, x, y):
        if target == 0:
            self.xy_0 = (x, y)
        elif target == 1:
            self.xy_1 = (x, y)

    def toggle_active(self):
        self.active = True if (self.active == False) else False


preset = Preset((0, 0), (0, 0))
print("String: ", preset.__str__())
print("Repr: ", preset.__repr__())

# KEYBOARD METHODS


def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(key.char))
    except AttributeError:
        print('special key {0} pressed'.format(key))


def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False


# MOUSE METHODS

def on_move(x, y):

    x = int(round(x))
    y = int(round(y))

    print('Pointer moved to {0}, {1}'.format(x, y))


def on_click(x, y, button, pressed):

    x = int(round(x))
    y = int(round(y))

    print('{0} at {1}'.format('Pressed' if pressed else 'Released', (x, y)))
    print(button, pressed)


def on_scroll(x, y, dx, dy):

    x = int(round(x))
    y = int(round(y))

    print('Scrolled {0} at {1}'.format('down' if dy < 0 else 'up', (x, y)))


# BLOCKING - Need to figure out how to get these working inside a MAIN loop using the tkinter GUI.

# with mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as mouse_listener:
#     mouse_listener.join()

# with keyboard.Listener(on_press=on_press, on_release=on_release) as keyboard_listener:
#     keyboard_listener.join()


# mouse_listener = mouse.Listener(on_click=on_click, on_press=on_press)
# mouse_listener.start()

# keyboard_listener = keyboard.Listener(on_press=on_press, on_release=on_release)
# keyboard_listener.start()
