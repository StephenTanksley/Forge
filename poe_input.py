from pynput.mouse import Button, Controller
from pynput import mouse, keyboard


class Mouse:
    def __init__(self, x=0, y=0, button=None, pressed=False):
        self.x = x
        self.y = y
        self.button = button
        self.pressed = pressed

    def __str__(self):
        return f'Current state:\nx-coordinate: {self.x}\ny-coordinate: {self.y}\nbutton: {self.button}\npressed: {self.pressed}'

    def __repr__(self):
        return f'[{self.x}, {self.y}, {self.button}, {self.pressed}]'

    def on_move(self, x, y):

        self.x = int(round(x))
        self.y = int(round(y))

        print('Pointer moved to {0}, {1}'.format(self.x, self.y))

    def on_click(self, x, y, button, pressed):

        x = int(round(x))
        y = int(round(y))

        print('{0} at {1}'.format(
            'Pressed' if pressed else 'Released', (self.x, self.y)))
        print(button, pressed)

    def on_scroll(self, x, y, dx, dy):

        x = int(round(x))
        y = int(round(y))

        print('Scrolled {0} at {1}'.format(
            'down' if dy < 0 else 'up', (self.x, self.y)))


mouse = Mouse()


class Keyboard:

    def __init__(self, key):
        self.key = key

    def __str__(self):
        return f'Current key: {self.key}'

    def __repr__(self):
        return [self.key]

    def on_press(self):
        try:
            print('alphanumeric key {0} pressed'.format(self.key.char))
        except AttributeError:
            print('special key {0} pressed'.format(self.key))

    def on_release(self):
        print('{0} released'.format(
            self.key))
        if self.key == keyboard.Key.esc:
            # Stop listener
            return False


# BLOCKING - Need to figure out how to get these working inside a MAIN loop using the tkinter GUI.

# with mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as mouse_listener:
#     mouse_listener.join()

# with keyboard.Listener(on_press=on_press, on_release=on_release) as keyboard_listener:
#     keyboard_listener.join()


# mouse_listener = mouse.Listener(on_click=on_click, on_press=on_press)
# mouse_listener.start()

# keyboard_listener = keyboard.Listener(on_press=on_press, on_release=on_release)
# keyboard_listener.start()
