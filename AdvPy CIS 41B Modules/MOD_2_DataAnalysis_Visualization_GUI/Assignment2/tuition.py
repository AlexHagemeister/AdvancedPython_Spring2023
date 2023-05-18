"""
Alex Hagemeister
Lab 2: numpy, matplotlib, and tkinter
CIS 41B, Spring 2023

FILE: tuition.py  

Contains the Tuition class, which reads data from the 3 input files and methods to analyze and plot the data.
The Tuition class processes data related to tuition costs, states, and years using NumPy arrays. 
It provides methods to plot:
    - the tuition distribution for the most recent year, 
    - the lowest tuition rates for a specified number of states, 
    - the tuition trends for states with the largest increases vs. the state with the smallest increase, 
and calculates statistics for the most current tuition rates, such as the minimum, maximum, mean, and median values. 

A decorator function is also included to print the return value of the decorated methods within the Tuition class.

"""

import matplotlib.pyplot as plt
import numpy as np


def print_return_value(func):
    """
    Decorator function to print the return value of the decorated function.
    """

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Return value: {result}")
        return result

    return wrapper


class Tuition:
    """
    A class to analyze and plot tuition data from the US College Board.
    """

    # Add filepaths to the 3 input files as class attributes
    COSTS_FILE = "costs.csv"
    STATES_FILE = "states.csv"
    YEARS_FILE = "years.csv"

    def __init__(self, costs_file=COSTS_FILE, states_file=STATES_FILE, years_file=YEARS_FILE):
        # Read data from the 3 input files and store them as numpy arrays using the read_data method
        self._costs, self._states, self._years = self.read_data(costs_file, states_file, years_file)

    def read_data(self, costs_file=COSTS_FILE, states_file=STATES_FILE, years_file=YEARS_FILE):
        """
        Reads data from the costs.csv, states.csv, and years.csv files.

        PARAM: filepaths to the 3 input files (defult values are the class attributes)
        RETURN: tuple of the data as numpy arrays.
        """

        ## Load costs data (as float type by default)
        costs = np.loadtxt(costs_file, delimiter=",")

        ## create array of indeces of nonzero rows
        # ALTERNATE VERSION: nonzero_idx_arr = np.where(costs[:, 0] != 0)
        nonzero_idx_arr = np.nonzero(costs[:, 0])

        ## Load states data and likewise assign a label to the view
        states = np.loadtxt(states_file, delimiter=",", dtype=str)

        ## Read years data (all on one line)
        with open(years_file, "r") as y_file:
            years = np.array([int(year[:4]) for year in (y_file.readline().strip().split(","))])

        # Return the data (views) for the nonzero rows using the nonzero_idx_arr
        return costs[nonzero_idx_arr], states[nonzero_idx_arr], years

    @print_return_value
    def plot_distribution(self):
        """
        Plots the distribution of tuition rates for the most recent year (2022-23).

        RETURN: the number of states being plotted.
        """
        # plt.figure()
        plt.hist(self._costs[:, -1])
        plt.title("Tuition Distribution for 2022-23", fontsize=18)
        plt.xlabel("Tuition Cost", fontsize=16)
        plt.xticks(rotation=45)
        plt.ylabel("Number of States", fontsize=16)
        # plt.show()
        return len(self._states)

    @print_return_value
    def plot_lowest_tuition(self, num_states):
        """
        Plots the tuition rates for the specified number of states with the lowest tuition rates.

        PARAM: num_states (int) - the number of states to plot
        RETURN: (str) - the name of the state with the lowest tuition rate
        """
        # argsort returns the indices that would sort an array
        lowest_states = np.argsort(self._costs[:, -1])[:num_states]
        sorted_tuition = self._costs[lowest_states, -1]
        sorted_states = self._states[lowest_states]

        # plt.figure()
        plt.bar(sorted_states, sorted_tuition)
        plt.title(f"Lowest {num_states} Tuition Rates for 2022-23 By State", fontsize=18)
        plt.xlabel("State", fontsize=16)
        plt.ylabel("Tuition Cost", fontsize=16)
        plt.xticks(rotation=45)
        # plt.show()
        return sorted_states[0]

    @print_return_value
    def plot_tuition_trends(self):
        """
        Plots the tuition trends for the 5 states with the largest tuition increases and the state with the smallest tuition increase.

        RETURN: the name of the state with the largest tuition increase.
        """
        # Calculate the difference between the first and last tuition rates for each state
        tuition_diff = self._costs[:, -1] - self._costs[:, 0]

        # get the index of the 5 largest increases and the smallest increase
        largest_increase_idx = np.argsort(tuition_diff)[-5:]
        smallest_increase_idx = np.argmin(tuition_diff)

        # NOTE: would tuition_diff.sort() work here? Efficiency?

        # plt.figure()
        for idx in largest_increase_idx:
            plt.plot(self._years, self._costs[idx], marker="o", label=self._states[idx])

        plt.plot(
            self._years,
            self._costs[smallest_increase_idx],
            marker="s",
            label=self._states[smallest_increase_idx],
            linestyle="--",
        )
        plt.title("Tuition Trends: 5 Largest vs. Smallest", fontsize=18)
        plt.xlabel("Year", fontsize=16)
        plt.xticks(self._years, rotation=45)
        plt.ylabel("Tuition Cost", fontsize=16)
        plt.legend()
        # plt.show()

        return self._states[largest_increase_idx[0]]

    @print_return_value
    def tuition_statistics(self):
        """
        Calculates the minimum, maximum, mean, and median of the most current tuition rates (2022-23) for all states.

        RETURN: a tuple containing the 4 values, rounded to the nearest whole number.
        """
        current_tuition = self._costs[:, -1]
        min_tuition = np.min(current_tuition)
        max_tuition = np.max(current_tuition)
        mean_tuition = np.mean(current_tuition)
        median_tuition = np.median(current_tuition)

        return (
            round(min_tuition),
            round(max_tuition),
            round(mean_tuition),
            round(median_tuition),
        )


if __name__ == "__main__":
    tuition = Tuition()
    tuition.plot_distribution()
    tuition.plot_lowest_tuition(5)
    tuition.tuition_statistics()
    tuition.plot_tuition_trends()
