'''
CIS 41A Fall 2022
Surajit A. Bose
Lab 5 Item Class
'''

class Item :
    ''' Specifies the different types of food/drink items for sale
        Prepackaged items like chips or boxed salad are in this parent class
    '''
    
    # Class attributes
    CRV_SMALL = 0.05
    CRV_LARGE = 0.10
    TAX = 0.0913
    
    # Instance methods
    def __init__ (self, name, id_num, price) :
        '''Instantiate objects of the class and define their attributes, duh'''
        self.name = name
        self.id_num = id_num
        self.price = price
        
    def __repr__ (self) :
        '''Return a string representation of the object'''
        return self.name + '(' + str(self.id_num) + '):' + str(f'{self.price:.2f}')
        
    # Two self-explanatory getter functions
    def getName(self) :
        return self.name
        
    def calcPrice(self) :
        return round(self.price, 2)


class HotFood(Item) :
    '''Subclass for prepared and heated food such as pizza
        Does not need its own __init__() as has no specialized attributes
    '''
        
    # Instance methods
    def __repr__(self) :
        '''Return a string representation of the object'''
        return super().__repr__() + ' - heated'
    
    def calcPrice(self):
        '''Hot food is taxed'''
        return round(self.price + self.price * Item.TAX, 2)
        

class Drink(Item) :
    '''Subclass for small or large drinks with a specialized attribute, size'''
    
    # Instance methods
    def __init__(self, name, id_num, price, size) :
        '''Instantiate objects of the class and define their attributes, duh'''
        super().__init__(name, id_num, price)
        if size.upper() == 'L' :
            self.crv = Item.CRV_LARGE
        elif size.upper() == 'S' :
            self.crv = Item.CRV_SMALL
        else :
            raise ValueError('Size must be L or S')
    
    def calcPrice(self) :
        '''Drink price includes CRV and tax on base price + CRV'''
        crv_price = self.price + self.crv
        return round(crv_price + crv_price * Item.TAX, 2)
