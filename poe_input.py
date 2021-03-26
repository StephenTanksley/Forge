from pynput.mouse import Button, Controller
from pynput import mouse, keyboard
from sys import exit


class Mouse(Controller):
    def __init__(self, bus, x=0, y=0, button=None, pressed=False):
        self.x = self.position
        self.y = self.position
        self.button = button
        self.pressed = pressed
        self._bus = bus
        self.last_click = None

    def __str__(self):
        return f'Current state:\nx-coordinate: {self.x}\ny-coordinate: {self.y}\nbutton: {self.button}\npressed: {self.pressed}'

    def __repr__(self):
        return f'[{self.x}, {self.y}, {self.button}, {self.pressed}]'

    def set_last_click(self, coordinates):
        self.last_click = (coordinates)

    def on_move(self, x, y):

        self.x = float(round(x, 2))
        self.y = float(round(y, 2))
        print('Pointer moved to {0}, {1}'.format(self.x, self.y))

    def on_click(self, *args):

        mouse_button = args[2]
        x = float(round(self.position[0], 2))
        y = float(round(self.position[1], 2))

        print(mouse_button, x, y)
        return [mouse_button, x, y]

    def on_scroll(self, x, y, dx, dy):

        x = float(round(x, 2))
        y = float(round(y, 2))

        print('Scrolled {0} at {1}'.format(
            'down' if dy < 0 else 'up', (self.x, self.y)))

    def drag(self, start, stop):
        self.position = start
        self.press(Button.left)


class Keyboard(Controller):

    def __init__(self, bus, key=None):
        self.key = key
        self.command = [0] * 2
        self._bus = bus

    def __str__(self):
        return f'Current key: {self.key}'

    def __repr__(self):
        return [self.key]

    def on_press(self, key):
        try:
            self.key = key
            print('alphanumeric key {0} pressed'.format(self.key.char))
        except AttributeError:
            print('special key {0} pressed'.format(self.key))

    def on_release(self, key):
        print('alphanumeric key {0} released'.format(
            self.key))
        if self.key == keyboard.Key.esc:
            # Stop listener
            print("Exiting keyboard listener. Goodbye!")
            exit()

# BLOCKING:

# with mouse.Listener(on_move=controller_mouse.on_move, on_click=controller_mouse.on_click, on_scroll=controller_mouse.on_scroll) as mouse_listener:
#     mouse_listener.join()

# with keyboard.Listener(on_press=controller_keyboard.on_press, on_release=controller_keyboard.on_release) as keyboard_listener:
#     keyboard_listener.join()


# NON-BLOCKING:

# MouseListener = mouse.Listener(
#     on_move=controller_mouse.on_move, on_click=controller_mouse.on_click, on_scroll=controller_mouse.on_scroll)
# MouseListener.start()

# KeyboardListener = keyboard.Listener(
#     on_press=controller_keyboard.on_press, on_release=controller_keyboard.on_release)
# KeyboardListener.start()
