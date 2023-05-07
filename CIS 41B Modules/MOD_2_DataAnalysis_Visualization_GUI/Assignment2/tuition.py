"""
Alex Hagemeister
Lab 2: numpy, matplotlib, and tkinter
CIS 41B, Spring 2023

tuition.py has a Tuition class, which has data from the 3 input files and methods to analyze and plot the data.
The user has 4 ways to see tuition data:
    1. A print out of the minimum, maximum, mean, and median of the 49 current tuition rates
    2. A plot of the distribution of tuitions in the most current year
    3. A plot to compare the lowest N current tuitions, where N is the user choice.
    4. A plot of the tuition trend of the 5 states with the largest tuition change and of the state with the smallest tuition
    change.

The Tuition class has methods to do the following:

a. Read in data from all 3 files and store them in appropriate data structures of your choice. 
Choose data structures that can shorten your code considerably.
    • The data files should be opened and read in one time only.
    • For states.csv and costs.csv: read in all lines into a container (the simplest way to read).
    Then find a way to use all but the 2nd row (no Alaska, since it doesn’t have data). 
    You should not have to create a new container without the 2nd row. 
    The new way (excluding the 2nd row) should be used for the rest of the methods.
    • For years.csv, simplify the year by storing only the first year out of each year string. For example, store “2022”
    from “2022-23”.

b. To help the user have an overview of current tuition rate across all the states, plot the tuition distribution.
    • Use the tuition of all states for 2022-23
    • The plot should have a title and axis labels as needed.
    • Return the number of states being plotted. This number should not be hard coded.

c. To help the user see which states will give the best return-on-investment for a 2-year college education, let the user
choose the number of states they want to see, and then plot the tuition of the correct number of states that have
the lowest tuition rate.
    • Accept a number as input argument. This is the number of states chosen by the user.
    • Choose an appropriate plot so that it’s easy for the user to see the difference in tuition among the states. 
    The tuition should be plotted in sorted order.
    • The plot should have a title and axis labels as needed.
    • The state names should be clearly marked with its tuition. The names should not overlap or be too small to
    view. The names should come from the Tuition object data, don’t hard code the names.
    • Return the name of the state with the lowest cost.

d. To help the user see which states have had the largest increase in tuition over the years, plot the tuition trend from
    the first to last available years for the 5 states with the largest increase in tuition, and then for reference, also plot
    the tuition trend of the one state with the smallest increase in tuition.
    • Choose a plot that will show the tuition trend of all years between the first and last available years.
    • The 5 state names with largest increase and 1 state name with smallest increase should be clearly labeled.
    And use a different marker for the 5 states vs 1 state so that the user can easily differentiate the 2 opposite
    trends.
    • The plot should have a title and axis labels as needed.
    • The state names should be clearly marked with its tuition. The names should not overlap or be too small to
    view. The names should come from the Tuition object data, don’t hard code the names.
    • Return the name of the state with the largest increase.

e. To help the user see some basic statistics on the tuition, find the minimum, maximum, mean, and median of the
most current tuition from all the states.
• Find all 4 statistical values for the 2022-23 year.
• Return a container with the 4 values, rounded to the nearest whole number.

In addition to the Tuition class, write a decorator that prints the return value of the function that it decorates.
Apply the decorator to the 4 methods in steps b-e, to use for debugging purpose.

Unit testing
    It’s highly recommended that you write the unit testing code for the Tuition class to confirm that it works, before moving
    to the ui.py file. The test code should have 5 lines:
    1 line to create the Tuition object, and 4 lines to call each of the 4 methods described above.

Lab 2 EC
    To really encourage you to do unit testing (a good practice in real life), there will be 2 pts EC if you show me your code
    and demo the 5 lines of test code running successfully, at office hour before class (10:30-11:20am) or right after class
    (1:30pm) on 5/2.
"""

import matplotlib.pyplot as plt
import numpy as np
import csv


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
        Returns the data as numpy arrays.
        """
        # Load costs data (as float type by default)
        alaska_idx = 1
        costs = np.loadtxt(costs_file, delimiter=",")

        # create array of indeces of rows where all costs are not equal to 0
        nonzero_idx_arr = np.where(costs[:, 0] != 0)
        # ALT: nonzero_idx_arr = np.nonzero(costs[:, 0])

        costs_view = costs[nonzero_idx_arr]

        # Load states data (state names, string type)
        states = np.loadtxt(states_file, delimiter=",", dtype=str)
        states_view = states[nonzero_idx_arr]

        # Read years data (data is all on one line)
        # with open(years_file, "r") as y_file:
        #     years = np.array([int(year[:4]) for year in (y_file.readline().strip().split(","))])
        years = np.loadtxt(years_file, delimiter=",", dtype=int, converters=lambda date_str: int(date_str[:4]))
        return costs_view, states_view, years

    @print_return_value
    def plot_distribution(self):
        """
        Plots the distribution of tuition rates for the most recent year (2022-23).
        Returns the number of states being plotted.
        """
        plt.figure()
        plt.hist(self._costs[:, -1], bins=10)
        plt.title("Tuition Distribution for 2022-23")
        plt.xlabel("Tuition")
        plt.ylabel("Number of States")
        plt.show()
        return len(self._states)

    @print_return_value
    def plot_lowest_tuition(self, num_states):
        """
        Plots the tuition rates for the specified number of states with the lowest tuition rates.
        Returns the name of the state with the lowest tuition rate.
        """
        # argsort returns the indices that would sort an array
        lowest_states = np.argsort(self._costs[:, -1])[:num_states]
        sorted_tuition = self._costs[lowest_states, -1]
        sorted_states = self._states[lowest_states]

        plt.figure()
        plt.bar(sorted_states, sorted_tuition)
        plt.title(f"Lowest {num_states} Tuition Rates for 2022-23")
        plt.xlabel("State")
        plt.ylabel("Tuition")
        plt.xticks(rotation=45)
        plt.show()
        return sorted_states[0]

    @print_return_value
    def plot_tuition_trends(self):
        """
        Plots the tuition trends for the 5 states with the largest tuition increases and the state with the smallest tuition increase.
        Returns the name of the state with the largest tuition increase.
        """
        # Calculate the difference between the first and last tuition rates for each state
        tuition_diff = self._costs[:, -1] - self._costs[:, 0]

        # get the index of the 5 largest increases and the smallest increase
        largest_increase_idx = np.argsort(tuition_diff)[-5:]
        smallest_increase_idx = np.argmin(tuition_diff)

        # NOTE: for thing in sorted(thing) tuition_diff.sort()

        plt.figure()
        for idx in largest_increase_idx:
            plt.plot(self._years, self._costs[idx], marker="o", label=self._states[idx])

        plt.plot(
            self._years,
            self._costs[smallest_increase_idx],
            marker="s",
            label=self._states[smallest_increase_idx],
            linestyle="--",
        )
        plt.title("Tuition Trends for States with Largest Increases and Smallest Increase")
        plt.xlabel("Year")
        plt.ylabel("Tuition")
        plt.legend()
        plt.show()

        return self._states[largest_increase_idx[0]]

    @print_return_value
    def tuition_statistics(self):
        """
        Calculates the minimum, maximum, mean, and median of the most current tuition rates (2022-23) for all states.
        Returns a tuple containing the 4 values, rounded to the nearest whole number.
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


# Test code
def main():
    tuition = Tuition()
    tuition.plot_distribution()
    tuition.plot_lowest_tuition(5)
    tuition.tuition_statistics()
    tuition.plot_tuition_trends()


if __name__ == "__main__":
    main()
    # tuition = Tuition()
