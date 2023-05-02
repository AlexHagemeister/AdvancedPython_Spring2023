# Person class and Student, Employee, Buddy subclasses

class Person :
    count = 0  # class attributes, shared by all objects of the class
    
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
        return self._age == other._age
    
    def __lt__(self, other) :
        return self._age < other._age    
    
    def getName(self) :
        ''' return object name '''
        return self._name
    
    
class Employee(Person) : 
    # need __init__ because we have salary special attribute that needs to be initialized
    def __init__(self, name, age=0, salary=0) :    # age can be default also
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
    # need __init__ because we have major special attribute that needs to be initialized
    def __init__(self, name, age, major='undeclared') :    
        super().__init__(name, age)    # call to __init__
        self._major = major
    
    # overriding happyBday so it behaves slightly differently
    def happyBday(self) :
        ''' increment age and print birthday greeting'''
        super().happyBday()             # use Person happyBday
        print("You're getting a free textbook")
        
class Buddy(Person) :
    # don't need __init__ because there's no special attribute that needs to be initialized        
        
    # overriding happyBday so it behaves slightly differently
    def happyBday(self) :
        ''' increment age and print birthday greeting'''
        super().happyBday()             # use Person happyBday
        print("I'm treating you to dinner")
        
        
        
    