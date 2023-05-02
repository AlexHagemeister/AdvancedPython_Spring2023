'''
CIS 41A Fall 2022
Surajit A. Bose
Lab 5 Inventory Class
'''

from item import Item, HotFood, Drink
import csv

class Inventory :
    ''' Inventory object has three attributes, all lists of Item objects:
        - list of generic Item objects (i.e., packaged foods)
        - list of specialized HotFood objects
        - list of specialized Drink objects
        (Drink and HotFood are subclasses of Item)
    '''
    
    # Class attributes
    INV_FILE = 'items.csv'
    
    # Instance methods
    def __init__ (self) :
        ''' Instantiate objects of the class and define their attributes, duh
            Read object attributes in from input file and call appropriate
            __init__() from Item class or one of its subclasses
        '''
        self.packaged = []
        self.hot = []
        self.drinks = []

        with open (Inventory.INV_FILE) as infile : 
            for line in csv.reader(infile) :
                num = int(line[0])
                if num in range(10, 20) :
                    self.packaged.append(Item(line[1], num, float(line[2])))
                elif num in range(20, 30) :
                    self.hot.append(HotFood(line[1], num, float(line[2])))
                elif num in range(30, 40) :
                    self.drinks.append(Drink(line[1], num, float(line[2]), line[3]))
                else :
                    raise ValueError('No item category found for ' + line[0])


    def __repr__(self) :
        '''Return a string representation of the object'''
        return '\n' + str(len(self.packaged)) + ' packaged foods, ' + str(len(self.hot)) + ' hot foods, ' + str(len(self.drinks)) + ' drinks' 
        
    # Various self-explanatory getter methods for class or object attributes
    def getInputFile() :
        return Inventory.INV_FILE
    
    def getPackagedItems(self) :
        return self.packaged
    
    def getHotItems(self) :
        return self.hot
    
    def getDrinks(self) :
        return self.drinks