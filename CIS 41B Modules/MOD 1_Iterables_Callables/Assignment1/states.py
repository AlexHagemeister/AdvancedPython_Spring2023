"""
Assignment #1: Population Data (iterables & callables)
Alex Hagemeister
CIS 41B - Advanced Python Programming
Spring Quarter 2023

file: states.py

    The States class stores state population data, and provides methods to look up the data.
    The user has 3 ways to look up data:
        1. Show states and population for a specific year, sorted by populaton 
        2. Show states with positive or negatve growth rate, sorted by state name 
        3. Show whether there is a drop in state populaton between 2 years
"""

import csv
import logging


class States:
    """Class to store state population data, and provide methods to look up the data"""

    def log_function_call(func):
        """A decorator that prints the name of the function that it decorates to a log file."""

        def wrapper(*args, **kwargs):
            # open the log file in append mode
            with open("logFile.txt", "a") as logFile:
                # write the function name to the log file
                logFile.write(f"{func.__name__} \n")
            # call the function being decorated and return the result
            return func(*args, **kwargs)

        return wrapper

    @log_function_call
    def __init__(self, inputFile: str = "statesPop.csv"):
        """
        Constructor to read the input file, and store the data in a data structure
        PARAM inputFile: the name of the input file to read
        """
        self._inputFile = inputFile
        self._lookupDict = {
            "state": 0,
            "1990": 1,
            "2000": 2,
            "2010": 3,
            "2020": 4,
            "2021": 5,
            "growth": 6,
        }
        self._populationData = {}  # dictionary to store the data

        # read the input file and store the data in a data structure.
        # For each line of data, uses the map() functon to convert the populaton numbers into integers.
        # Refers to the lookupDict to determine which column to use for the population numbers.
        with open(self._inputFile, "r") as inFile:
            reader = csv.reader(inFile)
            for row in reader:
                # convert the population numbers for current state to integers and store in a dictionary
                # filter out the state name and growth rate from the dictionary
                rowDict = dict(
                    map(
                        lambda key: (key, int(row[self._lookupDict[key]])),
                        filter(
                            lambda key: key != "state" and key != "growth",
                            self._lookupDict.keys(),
                        ),
                    )
                )
                # Store the growth rate as a float
                rowDict["growth"] = float(row[self._lookupDict["growth"]])
                # store the dictionary in the populationData dictionary, with the state name as the key
                self._populationData[row[self._lookupDict["state"]]] = rowDict

    @log_function_call
    def get_pops_for_year(self, year):
        """
        method to get the states with their population for a certain year,
        sorted in descending order by population
        PARAM year: the year to list the states by population
        YIELD a generator that can produce one tuple of (state name, population) at a time
        """
        try:
            # sort the dictionary by population in descending order
            sortedDict = sorted(
                self._populationData.items(),
                key=lambda item: item[1][year],
                reverse=True,
            )
            # yield the state and population for each item in the sorted dictionary
            for state, popDict in sortedDict:
                yield (state, popDict[year])

        except KeyError as e:
            print("Year not found.")
            raise e

    @log_function_call
    def getStatesByGrowth(self, positive):
        """
        generator method that yields a state and its growth rate,
        based on the user choice of positive or negative growth
        PARAM positive: True if user wants positive growth, False if user wants negative growth
        RETURN a generator that can produce one tuple of (state name, growth rate) at a time
        """
        # sort the dictionary by growth rate in descending order
        sortedByGrowthDict = sorted(
            self._populationData.items(),
            key=lambda item: item[1]["growth"],
            reverse=True,
        )
        # yield the state and growth rate for each item in the sorted dictionary
        for state, data in sortedByGrowthDict:
            if positive:
                if data["growth"] > 0:
                    yield (state, data["growth"])
            else:
                if data["growth"] < 0:
                    yield (state, data["growth"])

    @log_function_call
    def isPopulationDrop(self, startYear: str, endYear: str):
        """
        Checks whether at least one state has dropped in population between 2 given years
        PARAM startYear: the start year to check for population drop
        PARAM endYear: the end year to check for population drop
        RETURN True if at least one state has dropped in population, False otherwise
        """
        # check that the start year is before the end year
        if int(startYear) >= int(endYear):
            raise ValueError("Start year must be before end year")

        # check that the years are valid
        if (
            startYear not in self._lookupDict.keys()
            or endYear not in self._lookupDict.keys()
        ):
            raise ValueError("Invalid year")

        # check that the years are not the same
        if startYear == endYear:
            raise ValueError("Start year and end year cannot be the same")

        # check if any state has a population drop between the 2 years
        hasDrop = any(
            state[endYear] < state[startYear] for state in self._populationData.values()
        )

        return hasDrop

    @log_function_call
    def max_states(self):
        """returns the number of states in the data set"""
        return len(self._populationData)
