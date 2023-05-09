"""
Assignment #1: Population Data (iterables & callables)
Alex Hagemeister
CIS 41B - Advanced Python Programming
Spring Quarter 2023

File: ui.py

    The UI class has methods to recieve input from user and call the appropriate methods of the States class.
    The user has 3 ways to look up data:
        1. Show states and population for a specific year, sorted by populaton 
        2. Show states with positive or negatve growth rate, sorted by state name 
        3. Show whether there is a drop in state populaton between 2 years

"""

import states
import sys


class UI:

    """
    The UI class has methods to recieve input from user and call the appropriate methods of the States class.
    """

    def __init__(self):
        """
        Creates a States object with the default input file.
        Handles file exceptions by prompting user for a filename until there is a valid file to create the States object.
        NOTE: doesn't open any file to check for file exception, it’s the job of the States object open the file.
        """
        # if there is file exception, handle the exception by prompting the user for a filename until there is a valid file to create the States object
        while True:
            try:
                self._statesObj = states.States()
                break
            except FileNotFoundError:
                print("File not found.")
                filename = input("Enter a filename: ")
                self._statesObj = states.States(inputFile=filename)

    def printStatePopsForYear(self):
        """
        Prints the states and their population for a particular year.
        PARAM year: the year to list the states by population
        YIELD a generator that can produce one tuple of (state name, population) at a time
        """
        try:
            year = int(input("Enter year: "))
            numStates = int(input("Enter the number of states: "))

            if numStates <= 0:
                print("Must be greater than 0.")
                self.printStatePopsForYear()

            if numStates > self._statesObj.max_states():
                print("Input exceeds max number of states. Using max number of states.")
                numStates = self._statesObj.max_states()

            for state, pop in self._statesObj.getPopsForYear(str(year)):
                if numStates == 0:
                    break
                print(f"{state:<20} {pop:>10,d}")
                numStates -= 1

        except ValueError:
            print("Input must be numeric.")
            self.printStatePopsForYear()
        except KeyError:
            print("Invalid year.")
            self.printStatePopsForYear()

    def printStatesByGrowth(self):
        """
        Prints the states and their positive or negative growth.
        """
        print("\n\tp. positive \n\tn. negative \n")
        try:
            choice = input("Enter your choice: ")
            if choice.lower() == "p":
                positive = True
            elif choice.lower() == "n":
                positive = False
            else:
                print("Invalid choice.")
                self.printStatesByGrowth()
        except ValueError:
            print("Invalid choice.")
            self.printStatesByGrowth()

        print(f"Your choice: {choice}")
        for state, growth in self._statesObj.getStatesByGrowth(positive):
            print(f"{state:<20} {(growth * 100):>10.2f}%")

    def printPopulationDrop(self):
        """
        Prints whether there is at least 1 state that dropped in population between 2 given years.
        """
        try:
            startYear = input("Enter start year: ")
            endYear = input("Enter end year: ")
            if self._statesObj.isPopulationDrop(startYear, endYear):
                print(
                    f"Population drop in at least one state between {startYear} and {endYear}."
                )
            else:
                print(
                    f"No population drop in any state between {startYear} and {endYear}."
                )

        except ValueError:
            print("Invalid entry.")
            self.printPopulationDrop()

    def printMenu(self):
        """
        Prints a menu and keeps prompting the user until there’s a valid choice.
        """
        print(
            "\n\t1. View most populous states \n\t2. View growth in 2021 \n\t3. Check population drop \n\t4. Quit \n"
        )
        userSelection = input("Enter your selection: ")
        if userSelection not in "1234" and len(userSelection) != 1:
            print("Please enter a valid selection.")
            self.printMenu()
        return userSelection

    def run(self):
        """
        Loops to print the menu and process the user choice until the user chooses to quit.
        """
        # list of methods to call based on user choice
        taskList = [
            self.printStatePopsForYear,
            self.printStatesByGrowth,
            self.printPopulationDrop,
        ]
        try:
            userSelection = int(self.printMenu())
            if userSelection == 4:
                print("Goodbye.\n")
                sys.exit(0)
            taskList[userSelection - 1]()
        except (ValueError, IndexError):
            print("Invalid input.")

        self.run()


# Run the program
UI().run()
