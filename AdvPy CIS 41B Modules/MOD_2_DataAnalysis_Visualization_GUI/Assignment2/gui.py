"""
Alex Hagemeister
Lab 2: numpy, matplotlib, and tkinter
CIS 41B, Spring 2023

gui.py

This file contains 3 classes: a main window class, a dialog window class, and a plot window class. Each of the 3 window
classes is derived from an appropriate tkinter class.


1. The main window is an object of the main window class, and it appears when the app first comes up.
    • The window has a title, a line of text to explain the purpose of the application, 3 buttons, and the 4 statistics
    about the most current tuition.
    • The 3 buttons are for the user to choose: the overview tuition rates, the N lowest tuitions and states, or the 5
    largest changes and 1 smallest change in tuition and their states.
    • The buttons are placed side by side.
    • The 4 statistics are displayed 2 per line, with $ in front of the tuition value.
    • When the user clicks on the ‘Overview’ button or 'Largest Change' button: the main window creates a plot
    window with the appropriate plot.
    • When the user clicks on the ‘Lowest Cost’ button, the main window creates a dialog window to ask the user for
    a choice of number of states to be displayed. When the user selects a choice, the dialog window closes and the
    main window creates the plot window with the appropriate plot.
    • When the user clicks X to close the main window, all other windows of the app should close.

2. The plot window is an object of the plot window class. The plot window is created by the main window:
    • The plot window must be a tkinter window that works with matplotlib, and not an independent matplotlib
    window.
    • There should be one plot window class that can display all 3 plots of the Tuition class. Do not create different
    plot window classes.
    • The user can click X to close the plot window, or the user can leave the window open and go to the main
    window to select another choice. This means there can be multiple plot windows opened if the user chooses to
    keep them open.   


3. The dialog window is an object of the dialog window class. The window is created by the main window when the
user selects the ‘Largest Change’ button.

    • The window has a radio button for the 4 number choices that the user has.
    • The buttons should be lined up on the left of the window, and the first button is selected by default.
    • There is a button that the user clicks to lock in their number choice.
    • When the dialog window opens, all other windows should be disabled so that the user cannot use the main window 
    to select another choice.
    • The user has 2 options with the dialog window:
        - click the button to lock in the radio button choice
        - click X to close the dialog window and not select a choice

Interaction between the main window and the dialog window:
    • If the user clicks the button to lock in their selection, then the dialog window closes, and the main window can
    get the user's number choice of N. Based on the user's choice, the main window creates a plot window with N
    lowest tuition rates and their states.
    Note that the dialog window should not create the plot window. The dialog window's job is to dialog with the
    user to get the user's choice. The processing of the user's choice is the job of the main window object.
    • If the user clicks X on the dialog window, then dialog window closes and no plot window appears. The user can
    then go to the main window to make another selection. 

Exception handling
    • During GUI start up, data will be read in from the 3 input files. If a file open is not successful, a messagebox
    window lets the user know that there is a file open error, with the specific file name.
    • When the user closes the messagebox window, the main window closes and the application terminates.

"""

import tkinter as tk
import matplotlib

matplotlib.use("TkAgg")
import tkinter.messagebox as tkmb
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # Canvas widget
import matplotlib.pyplot as plt  # normal import of pyplot to plot
from matplotlib.figure import Figure
from tuition import Tuition


class MainWindow(tk.Tk):
    def __init__(self):
        # call the parent class constructor
        super().__init__()

        self.title("Tuition Analysis")
        self.geometry("450x200")
        self.tuition = Tuition()

        ## Create the widgets for the main window

        # create the label for the purpose of the application
        tk.Label(self, text="Select a tuition analysis option:").grid(row=0, column=0, columnspan=3, sticky=tk.W)

        # get the statistics from the Tuition object to display as labels
        min_tuition, max_tuition, mean_tuition, median_tuition = self.tuition.tuition_statistics()

        # create labels for the statistics
        tk.Label(self, text=f"Lowest tuition: ${min_tuition}").grid(row=2, column=0, sticky=tk.W)
        tk.Label(self, text=f"Highest tuition: ${max_tuition}").grid(row=2, column=1, sticky=tk.W)
        tk.Label(self, text=f"Mean tuition: ${mean_tuition}").grid(row=3, column=0, sticky=tk.W)
        tk.Label(self, text=f"Median tuition: ${median_tuition}").grid(row=3, column=1, sticky=tk.W)

        # Create buttons and their commands
        btn_overview = tk.Button(
            self, text="Overview", command=lambda: PlotWindow(self, self.tuition.plot_distribution)
        )
        btn_overview.grid(row=1, column=0)

        btn_lowest_cost = tk.Button(
            self, text="Lowest Cost", command=lambda: DialogWindow(self, self.tuition.plot_lowest_tuition)
        )
        btn_lowest_cost.grid(row=1, column=1)

        btn_largest_change = tk.Button(
            self, text="Largest Change", command=lambda: PlotWindow(self, self.tuition.plot_tuition_trends)
        )
        btn_largest_change.grid(row=1, column=2)


class PlotWindow(tk.Toplevel):
    def __init__(self, parent, plot_func, *args):
        super().__init__(parent)
        self.title("Tuition Plot")
        self.geometry("600x400")

        fig = Figure(figsize=(6, 4), dpi=100)
        plot_func(*args)

        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=0)


class DialogWindow(tk.Toplevel):
    def __init__(self, parent, plot_func):
        super().__init__(parent)
        self.geometry("200x200")
        self.parent = parent
        self.plot_func = plot_func
        self.title("Select Number of States")

        self.num_var = tk.IntVar()
        self.num_var.set(5)

        tk.Radiobutton(self, text="5", variable=self.num_var, value=5).grid(row=0, column=0, sticky=tk.W)
        tk.Radiobutton(self, text="10", variable=self.num_var, value=10).grid(row=1, column=0, sticky=tk.W)
        tk.Radiobutton(self, text="15", variable=self.num_var, value=15).grid(row=2, column=0, sticky=tk.W)
        tk.Radiobutton(self, text="20", variable=self.num_var, value=20).grid(row=3, column=0, sticky=tk.W)

        tk.Button(self, text="Select", command=self.select).grid(row=4, column=0, sticky=tk.W)

        self.protocol("WM_DELETE_WINDOW", self.close)

    def select(self):
        PlotWindow(self.parent, self.plot_func, self.num_var.get())
        self.destroy()

    def close(self):
        self.destroy()


if __name__ == "__main__":
    # create the main window object
    main_window = MainWindow()
    main_window.mainloop()
