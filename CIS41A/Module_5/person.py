class Person :
    '''Creates Person objects and specifies their attributes and behavior'''
    
    def __init__ (self, name, age = 0) :
        '''Create a new Person with name and age'''
        self.name = name
        self.age = int(age)

    def __repr__(self):
        return self.name + ", " + str(self.age)
    
    def happyBday(self) :
        '''increments age and wishes name a happy birthday'''
        self.age += 1
        print ("Happy Birthday, " + self.name + " You're " + str(self.age) + " today")

