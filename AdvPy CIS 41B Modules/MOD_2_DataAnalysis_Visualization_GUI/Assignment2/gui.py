"""
Alex Hagemeister
Lab 2: numpy, matplotlib, and tkinter
CIS 41B, Spring 2023
FILE: gui.py

This script is a graphical user interface (GUI) for analyzing college tuition data. 

It uses the tkinter library for the GUI and matplotlib for plotting the data. 
The script imports tuition data from the Tuition class, which is defined in a separate file called 'tuition.py'. 
The main window displays statistics of the tuition data, such as the lowest, highest, mean, and median tuition costs. 

There are three buttons to create different plots: 
    an overview plot of the distribution of tuition costs, 
    a plot for the lowest tuition costs, 
    and a plot for the largest change in tuition costs. 

The lowest tuition costs plot allows users to select the number of states to include in the plot. 

Exception handling: 
    If file errors occur when reading the tuition data an appropriate error message is displayed. 
    If the user closes the main window, the program exits.

"""

import tkinter as tk
import matplotlib

matplotlib.use("TkAgg")
import tkinter.messagebox as tkmb
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from tuition import Tuition


class MainWindow(tk.Tk):
    def __init__(self):
        # call the parent class constructor
        super().__init__()
        self.title("Tuition Cost Analysis Program")
        # Try to create the Tuition object. If there is a file open error,
        # display the error and exit the program.
        try:
            self.tuition = Tuition()
        except FileNotFoundError as e:
            tkmb.showerror("File Open Error", str(e), parent=self)
            self.destroy()
            raise SystemExit

        ###### Create the widgets for the main windown ######

        # create the label for the purpose of the application
        purpose_label = tk.Label(self, text="Yearly College Tuition", fg="blue", font=("Helvetica", 20))
        purpose_label.grid(row=0, column=0, columnspan=3, sticky="we")

        # get the statistics from the Tuition object to display as labels
        min_tuition, max_tuition, mean_tuition, median_tuition = self.tuition.tuition_statistics()

        # create labels for the statistics
        cell_padding = 20
        tk.Label(self, text=f"Lowest tuition: ${min_tuition}", fg="green").grid(
            row=2, column=0, columnspan=2, sticky="w", padx=cell_padding, pady=4
        )
        tk.Label(self, text=f"Highest tuition: ${max_tuition}", fg="green").grid(
            row=2, column=1, columnspan=2, sticky="e", padx=cell_padding, pady=4
        )
        tk.Label(self, text=f"Mean tuition: ${mean_tuition}", fg="green").grid(
            row=3, column=0, columnspan=2, sticky="w", padx=cell_padding, pady=4
        )
        tk.Label(self, text=f"Median tuition: ${median_tuition}", fg="green").grid(
            row=3, column=1, columnspan=2, sticky="e", padx=cell_padding, pady=4
        )

        # Create buttons and their commands (passing references to appropriate functions)
        btn_overview = tk.Button(
            self, text="Overview", command=lambda: PlotWindow(self, self.tuition.plot_distribution)
        )
        btn_overview.grid(row=1, column=0, pady=cell_padding)

        btn_lowest_cost = tk.Button(
            self, text="Lowest Cost", command=lambda: DialogWindow(self, self.tuition.plot_lowest_tuition)
        )
        btn_lowest_cost.grid(row=1, column=1, pady=cell_padding)

        btn_largest_change = tk.Button(
            self, text="Largest Change", command=lambda: PlotWindow(self, self.tuition.plot_tuition_trends)
        )
        btn_largest_change.grid(row=1, column=2, pady=cell_padding)


class PlotWindow(tk.Toplevel):
    def __init__(self, parent, plot_func, *args, **kwargs):
        super().__init__(parent)
        self.title("Tuition Plot")

        fig = plt.figure(figsize=(6, 4), dpi=100)
        plot_func(*args, **kwargs)

        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.get_tk_widget().grid(row=0, column=0)
        canvas.draw()


class DialogWindow(tk.Toplevel):
    def __init__(self, parent, plot_func):
        super().__init__(parent)
        self.parent = parent
        self.plot_func = plot_func
        self.title("Select Number of States")

        purpose_label = tk.Label(self, text="Select Number of States:", font=("Helvetica", 16))
        purpose_label.grid(row=0, column=0)

        self.num_var = tk.IntVar()
        self.num_var.set(5)

        tk.Radiobutton(self, text="5", variable=self.num_var, value=5).grid(row=1, column=0)
        tk.Radiobutton(self, text="10", variable=self.num_var, value=10).grid(row=2, column=0)
        tk.Radiobutton(self, text="15", variable=self.num_var, value=15).grid(row=3, column=0)
        tk.Radiobutton(self, text="20", variable=self.num_var, value=20).grid(row=4, column=0)

        tk.Button(self, text="Select", command=self.select).grid(row=5, column=0)

        self.protocol("WM_DELETE_WINDOW", self.close)

    def select(self):
        PlotWindow(self.parent, self.plot_func, self.num_var.get())
        self.destroy()

    def close(self):
        self.destroy()
        self.quit()


if __name__ == "__main__":
    # main_window = MainWindow()
    # main_window.mainloop()
    main_window = MainWindow().mainloop()
