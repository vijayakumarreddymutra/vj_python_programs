
'''
import tkinter as tk

root = tk.Tk()

text = tk.Text(root)
text.pack()

def undo(event):
    print("Ctrl + Z Pressed")
    return "break"

text.bind("<Control-z>", undo)

root.mainloop()



import keyboard

undo_stack: list = []

def undo():
    if undo_stack:
        print("Undo:", undo_stack.pop())
    else:
        print("Nothing to undo")

print("Press Ctrl + Z")

keyboard.add_hotkey("ctrl+z", undo)

keyboard.wait()
'''



