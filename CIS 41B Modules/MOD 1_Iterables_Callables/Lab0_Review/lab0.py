# Lab 0: Review CIS 41A
# Name: Alex Hagemeister

"""
This program reads a CSV file containing population data for cities in Santa Clara County, 
and prints the population for each city in a specified year.
"""

from collections import defaultdict

YEARS_ARR = [2000, 2010, 2020]  # years associated with population data
POP_FILE = 'cities.csv'         # CSV file w/ pop data

class Cities :
    '''Population for cities of Santa Clara County'''

    def __init__(self, popFileName=POP_FILE, yearsArr=YEARS_ARR):
        '''
        Read from CSV file (popFileName) to initialize population data

        PARAM popFileName=POP_FILE: name of CSV file 
        PARAM yearsArr=YEARS_ARR: list of years associated with population data
        '''

        self._popDataDict = {}              # dictionary of city names and population data
        self._yearsArr = yearsArr           # list of years associated with population data
        self._popFileName = popFileName

        cityNameIdx = 0     # explicit index to avoid magic numbers  

        try:
            with open(self._popFileName, 'r') as inFile:
                for line in inFile:
                    # Strip off the newline character and split the line into a list
                    cityPopByYrList = line.strip().split(',')
                    # Get the city name from the listified line
                    cityName = cityPopByYrList[cityNameIdx]
                    # Use a defaultdict to initialize population data for each city
                    self._popDataDict[cityName] = defaultdict(lambda: "No population data")
                    # Add population data for each year from the listified line, skipping the city name
                    for i, year in enumerate(self._yearsArr, start = 1):
                        self._popDataDict[cityName][year] = int(cityPopByYrList[i])

        except FileNotFoundError:
            print('City population file not found')
            exit()
    
    def printYear(self, year):
        '''
        Print population for each city in the specified year
        PARAM year: year to print population data for
        RETURN flag: True upon successful print, False otherwise
        '''
        flag = False
        header = f'\nCity populations for year {year}:'
        print(header)
        # print the city & population for each city in year
        for city, popDict in self._popDataDict.items():
            # <20: left justify w/ 20-char width. >10: right justify w/ 10-char width
            print(f'{city:<20} {popDict[year]:>10}')
            flag = True

        return flag # Not necessary, but I feel like it's good practice to return *something*

def main():
    
    C = Cities()      
    C.printYear(2020)
    C.printYear(2000)
    C.printYear(10)
    C.printYear('a')

if __name__ == '__main__':
    main()