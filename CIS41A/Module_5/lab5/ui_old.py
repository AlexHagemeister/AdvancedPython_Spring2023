from inventory import Inventory
import re

class UI :
    def __init__(self):
        try :
            self.for_sale = Inventory()
            self.menu = dict()
        except FileNotFoundError :
            filename = Inventory.getInputFile()
            print('File ' + filename + ' not found')
        except ValueError as e:
            print('Error:', str(e))
            
    def addItemsToMenu(some_dict, some_set) :
        num = len(some_dict) + 1
        some_dict.update((k, v) for k, v in enumerate(some_set, start = num))
    
    def createMenu(self) :
        UI.addItemsToMenu(self.menu, self.for_sale.packaged)
        UI.addItemsToMenu(self.menu, self.for_sale.hot)
        UI.addItemsToMenu(self.menu, self.for_sale.drinks)
            
    
        
    def printMenu(self) :
        print(self.for_sale)
        num = 1
        print('\n       Packaged Foods')
        for item in self.for_sale.packaged:
            m = re.search('([A-Za-z\s]+)[^:]+:([\d\.]+)', str(self.menu[num]))
            print(f'{num} {m.group(1):18s} $ {m.group(2):6s}')
            num += 1
        print('       Hot Foods') 
        for item in self.for_sale.hot:
            m = re.search('([A-Za-z\s]+)[^:]+:([\d\.]+)', str(self.menu[num]))
            print(f'{num} {m.group(1):18s} $ {m.group(2):6s}')
            num += 1
        print('       Drinks')
        for item in self.for_sale.drinks:
            m = re.search('([A-Za-z\s]+)[^:]+:([\d\.]+)', str(self.menu[num]))
            print(f'{num} {m.group(1):18s} $ {m.group(2):6s}')
            num += 1
'''
    def prettyPrint(some_dict, num) :
        m = re.search('([A-Za-z\s]+)[^:]+:([\d\.]+)', str(some_dict[num]))
        print(f'{num} {m.group(1):18s} $ {m.group(2):6s}')
        


        choice = UI.prettyPrint(self.for_sale.packaged, choice_num)
        print('       Hot Foods') 
        choice = UI.prettyPrint(self.for_sale.hot, choice_num)        
        print('       Drinks')
        choice = UI.prettyPrint(self.for_sale.drinks, choice_num)
'''

            
print()
my_UI = UI()
my_UI.createMenu()
my_UI.printMenu()