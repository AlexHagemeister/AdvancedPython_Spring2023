# Person class

"""
a class is a user defined data type:
it has data and methods

Data also called attribute:
- local variables: scope only within the method that it's defined
- instance variables: start with self. 
                   scope within the object, it lasts as long as the object lasts
                   accessible automatically by all methods of the class
- class variables: scope within the entire class
                accessible by all objects of that class
                almost like "global" variables within one class

Methods define the behavior of the class:
- private methods: called only by other methods of the class
- public methods: called by entities outside of the class
      accessor or getter
      mutator or setter
      
- special methods / magic methods / dunders (double underscore methods)
    in the format:  __name__
    the caller never calls them by name, instead the caller uses
    special conditions to let python to call these methods
"""

class Person :
    count = 0   # update?
    
    # __init__'s job is to initialize *all* instance attributes
    # either with some known valid data or with some default values
    def __init__(self, name, age=0) :
        self._name = name
        self._age = int(age)    # let exception happen to force user to use an int
        Person.count += 1
       
    def __repr__(self) :
        return self._name + ", age " + str(self._age) + ", " + str(self.count)
    
    def happyBday(self) :
        ''' increment age and print birthday greeting'''
        self._age += 1
        print("Happy Birthday,", self._name, "You're", self._age, "today")
        
    def __eq__(self, other) :
        return self.age == other.age :

    def __lt__(self, other) :
        return self._age < other._age    
    
    def getName(self) :
        ''' return object name '''
        return self._name
    
    
class Employee(Person) : 
    # need __init__ because we have salary special attribute that needs to be initialized
    def __init__(self, name, age, salary=0) :    # age can be default also
        super().__init__(name, age)    # call to __init__
        self._salary = float(salary)
        
    # don't need __repr__ because we can re-use it from Person
    
    # overriding happyBday so it behaves slightly differently
    def happyBday(self) :
        ''' increment age and print birthday greeting'''
        self._age += 1
        print("Happy Birthday,", self._name)
     
     # adding new method for Employee
    def salary(self) :
        ''' print the salary '''
        print("Salary =", self._salary)
        
class Student(Person) :

    def __init__(self, name, age = 0, major = 'undeclared') :
        super().__init__(name, age)
        self._major = major
        
    def happyBday(self) :
        ''' increment age and print birthday greeting'''
        super().happyBday(self)
        print("You're getting a free textbook")
        
class Buddy (Person) :

    def happyBday (self) :
        super().happyBday(self)
        print("I'll treat you to dinner")
    
