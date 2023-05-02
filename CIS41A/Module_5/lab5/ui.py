'''
CIS 41A Fall 2022
Surajit A. Bose
Lab 5 UI Class
'''

from inventory import Inventory
import re

class UI :
    ''' UI object has two attributes:
        - for_sale, list of food items in inventory
        - menu, dictionary of key-value pairs 
            - key: ordinal number indicating position on printed menu
            - value: food item of Item class or one of its subclasses
    '''
            
    # Internal helper functions called only by methods of this class
    def menuBuildHelper(some_dict, some_list) :
        ''' Add key-value pairs to UI dictionary
            key is ordinal number indicating position in printed menu
            value is sequential from list of food objects of specific (sub)class
            @param some_dict dictionary to which key-value pairs are added
            @param some_list list from which values are added sequentially
        '''
        for item in some_list :
            num = len(some_dict) + 1 
            some_dict[num] = item

    def menuPrintHelper(some_dict, some_list) :
        ''' Print key-value pairs from UI dictionary to screen 
            in proper format, iff they belong to the appropriate subclass 
            @param some_dict UI dictionary attribute
            @param some_list list of food objects of specific (sub)class
        '''
        for k,v in sorted(some_dict.items()) :
            if v in some_list: 
                m = re.search('([A-Za-z\s]+)[^:]+:([\d\.]+)', str(v))
                print(f'{k:d}. {m.group(1):18s} $  {m.group(2):6s}')

    # Instance methods
    def __init__(self):
        '''Instantiate objects of the class and define their attributes, duh'''
        try :
            self.for_sale = Inventory()
            print(self.for_sale)
            self.menu = dict()
            UI.menuBuildHelper(self.menu, self.for_sale.getPackagedItems())
            UI.menuBuildHelper(self.menu, self.for_sale.getHotItems())
            UI.menuBuildHelper(self.menu, self.for_sale.getDrinks())
        except FileNotFoundError :
            filename = Inventory.getInputFile()
            print('File ' + filename + ' not found')
        except ValueError as e:
            print('Error:', str(e))
        
    def printMenu(self) :
        '''Display the menu onscreen'''
        print('\n       Packaged Foods')
        UI.menuPrintHelper(self.menu, self.for_sale.getPackagedItems())
        print('       Hot Foods') 
        UI.menuPrintHelper(self.menu, self.for_sale.getHotItems())
        print('       Drinks')
        UI.menuPrintHelper(self.menu, self.for_sale.getDrinks())
            
    def run(self) :
        '''Code driver'''
        end = False
        while not end:
            self.printMenu()
            instring = input("\nEnter one or more choice numbers: ")
            choices = re.findall('\-?\d+', instring)
            good = []
            bad = []
            total = 0
            for c in choices :
                ch = int(c)
                if ch in self.menu :
                    item = self.menu[ch]
                    cost = item.calcPrice()
                    print(f'{ch:d}. {item.getName():18s} ${cost:6.2f}')
                    total += cost
                else : 
                    bad.append(ch)
            if total:
                print(f'Total including CRV and tax if applicable: ${total:.2f}')
            if bad :
                print('Invalid choice', end = '')
                if len(bad) > 1 :
                    print('s', end = '')
                print(':', end = ' ')
                for num in bad:
                    print(num, end = ' ')
                print()
            instring = input('\nBuy more? Y/N: ')
            while instring.upper() not in ('YN') :
                instring = input('Please choose Y to buy more, N to quit: ')
            if instring.upper() == 'N' :
                print('Thank you, come again!\n')
                end = True
            

my_UI = UI()
my_UI.run()
