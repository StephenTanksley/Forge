from tkinter import ttk
from tkinter import *
# from pynput import mouse, keyboard
from poe_script import Preset
# from poe_input import Mouse, Keyboard


# def calculate(*args):
#     try:
#         value = float(feet.get())
#         meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
#     except ValueError:
#         pass

# GUI down here

class POEForge:
    def __init__(self, root):
        root.title("Path of Exile Forge")

        preset = Preset((0, 0), (0, 0), False)
        # test_mouse = Mouse()
        # test_keyboard = Keyboard()

        mainframe = ttk.Frame(root, borderwidth=5, padding="5 5 15 15")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        target_1 = StringVar()
        ttk.Label(mainframe, width=7, textvariable=target_1).grid(
            column=2, row=1, sticky=(W, E))

        target_2 = StringVar()
        ttk.Label(mainframe, textvariable=target_2).grid(
            column=2, row=2, sticky=(W, E))

        # ttk.Button(mainframe, text="Calculate", command=calculate).grid(
        #     column=3, row=3, sticky=W)

        ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
        ttk.Label(mainframe, text="is equivalent to").grid(
            column=1, row=2, sticky=E)
        ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

# feet_entry.focus()
# root.bind("<Return>", calculate)


# This is where I'm binding the input controls for the application.

# mouse_listener = mouse.Listener(
#     on_move=test_mouse.on_move, on_click=test_mouse.on_click, on_scroll=test_mouse.on_scroll)
# mouse_listener.start()

# keyboard_listener = keyboard.Listener(
#     on_press=test_keyboard.on_press, on_release=test_keyboard.on_release)
# keyboard_listener.start()


# This is the invocation function. Kinda like the render in React. I'm choosing to encapsulate the application in a class.

root = Tk()
POEForge(root)
root.mainloop()
