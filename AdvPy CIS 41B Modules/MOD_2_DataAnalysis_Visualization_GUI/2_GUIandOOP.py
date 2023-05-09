# Module 2 exercise: GUI with OOP

import tkinter as tk

# 1. Create a main window class which is derived from the Tk class.
#    Inside the main window add a button with the name "say hi"
#    such that when clicked, it creates a toplevel window.
#
# 2. Create a display window class which is derived from the Toplevel class.
#    This window displays a "hi" string.
#
# 3. Extra: add to the display window


class DisplayWin(tk.Toplevel):
    def __init__(self, master, num):
        super().__init__(master)
        self._num = num
        tk.Label(self, text="Hi").grid()
        tk.Button(self, text="Add 2", command=self.add_2).grid()

    def add_2(self):
        self._num += 2
        self.destroy()


class MainWin(tk.Tk):
    def __init__(self):
        # Call the constructor of the parent class
        super().__init__()
        # Add a button to the main window and bind it to a callback function
        tk.Button(self, text="Say Hi", command=self.say_hi).grid()

    @property
    def num(self):
        return self._num
    
    def say_hi(self):
        # Create a display window
        w = DisplayWin(self, 5)
        self.wait_window(w)
        print(w.num)





app = MainWin()
app.mainloop()

