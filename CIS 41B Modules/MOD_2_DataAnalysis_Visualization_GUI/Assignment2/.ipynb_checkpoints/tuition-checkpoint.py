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

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


class Tuition:
    def __init__(self, costs_file, states_file, years_file):
        self.costs = pd.read_csv(costs_file, header=0).iloc[:, 1:]  # remove Alaska
        self.states = pd.read_csv(states_file, header=None)[0].iloc[1:].tolist()  # remove Alaska
        self.years = pd.read_csv(years_file, header=None)[0].str.split('-').str[0].tolist()

    def get_current_tuition_stats(self):
        tuition_2022 = self.costs.iloc[:, -1]
        return [int(round(tuition_2022.min())), int(round(tuition_2022.max())), int(round(tuition_2022.mean())),
                int(round(tuition_2022.median()))]

    def plot_tuition_distribution(self):
        tuition_2022 = self.costs.iloc[:, -1]
        num_states = len(tuition_2022)
        plt.hist(tuition_2022, bins=20)
        plt.title("Tuition Distribution in 2022-23")
        plt.xlabel("Tuition")
        plt.ylabel("Number of States")
        plt.show()
        return num_states

    def plot_lowest_tuition_states(self, n_states):
        tuition_2022 = self.costs.iloc[:, -1]
        lowest_tuition_states = tuition_2022.nsmallest(n_states)
        lowest_tuition_states_names = self.costs.iloc[lowest_tuition_states.index].index.tolist()
        plt.bar(lowest_tuition_states_names, lowest_tuition_states)
        plt.title(f"Tuition for the {n_states} States with the Lowest Tuition in 2022-23")
        plt.xlabel("State")
        plt.ylabel("Tuition")
        plt.xticks(rotation=45, ha='right')
        plt.show()
        return self.states[tuition_2022.idxmin()]

    def plot_tuition_trend(self):
        tuition_diff = self.costs.diff(axis=1).iloc[:, 1:]
        largest_increase_states = tuition_diff.sum().nlargest(5).index.tolist()
        smallest_increase_state = tuition_diff.sum().nsmallest(1).index[0]
        for state in largest_increase_states:
            plt.plot(self.years, self.costs.loc[self.states.index(state), :], label=state, marker='o')
        plt.plot(self.years, self.costs.loc[self.states.index(smallest_increase_state), :], label=smallest_increase_state, marker='s')
        plt.title("Tuition Trend from First to Last Available Years")
        plt.xlabel("Year")
        plt.ylabel("Tuition")
        plt.legend(loc="best")
        plt.show()
        return self.states[self.costs.diff(axis=1).iloc[:, 1:].sum().idxmax()]
