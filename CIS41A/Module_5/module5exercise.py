# Module 5 exercise: inheritance and regular expression


############# superclass ##############
# 1. Use the file person.py that contains the Person class from exercise 4. 
# This is the driver code for person.py from exercise 4

from person1 import Person, Student, Employee #, Buddy

# create a person 
person1 = Person("Fred")
bff = Person("Wilma")

bff.happyBday()   # print: Happy Birthday, Wilma You're 1 today
bff.happyBday()   # print: Happy Birthday, Wilma You're 2 today   
print(bff)

if person1 == bff:    # compare age
   print("Same age")
elif person1 < bff:    
   print(person1.getName(), "is younger")
else:
   print(bff.getName(), "is younger")
print()
  

############## inheritance and subclasses ##############

# 3. Add 3 subclasses of the Person class:
# Employee: 
# - add a new optional field called salary,
#   default to 0
# - override the happyBday method so it adds 1
#   to the age and prints "Happy Birthday"
# - add a salary() method that prints the
#   employee's salary
#              
# create an employee
e = Employee("Pebbles", 20, 15)
print(e)
e.salary()
e.happyBday()
print()

# Student: 
# - add a new optional field called major,
#   default to "undeclared"
# - override the happyBday method so it does 
#   what the Person class method does, and 
#   then print "You're getting a free textbook"
#
# create a student
s = Student("Bam Bam", 18, "music")
print(s)
s.happyBday()
print()

# Buddy: 
# - no additional field
# - override the happyBday method so it does 
#   what the Person class method does, and 
#   then print "I'll treat you to dinner"
#
# create a buddy
b = Buddy("Bud", 22)
print(b)
b.happyBday()
print()


if s == b:    # compare age
   print("Same age")
elif s < b:    
   print(s.getName(), "is younger")
else:
   print(b.getName(), "is younger")
print()

  
# polymorphism
def bdayWish(p):     # a polymorphic function
   p.happyBday()
    
# What is printed?  # the birthday greeting for the appropriate object
bdayWish(bff)    
bdayWish(e)      
bdayWish(s)      
bdayWish(b)

print()


############### regular expression ###############

import re

# Given the following data:
str1 = "The answer is 42"
str2 = "What... is the air speed of an unladen swallow?"
str3 = "3.15; 2.383 and 11.039*2.77  1257.11"
str4 = "2020 / 08 / 14"
inList = [str1, str2, str3, str4]

# 1. Write regex to print the string if the string has:
# a. a digit

for str in inList :
    if re.search('\d', str) :
        print(str)

print()


# b. a number that's at least 3 digit long


for str in inList :
    if re.search('\d{3}', str) : 
        print(str)
print()


# c. no letters

for str in inList :
    m = re.search('^[^A-Za-z]+$', str)
    if m :
       print (str)
print()


# 2. Write a regex to print 
# a. the 3 numbers of str4
str4 = "the day 2020 / 08 / 14  is a random day"

print(re.findall('\d+', str4))

for m in re.finditer('\d+', str4) :
    print(m, end = ' ')
    print(m.group(), end = ' ')
    print (m.start())


# b. the start location of the 3 numbers of str4

print()

# 3. Write a regex to print:
# a. the first word of str2
str2 = "What... is the air speed of an unladen swallow?"

m = re.search('[A-Za-z]+', str2)
print(m.group())

print()

# b. the last word of str2


m = re.search('([A-Za-z]+)[^A-Za-z]*$', str2)
print(m.group(1))

# c. both the first and last words of str2

m = re.search('([A-Za-z]+).*[^A-Za-z]([A-Za-z]+)[^A-Za-z]*$', str2)

print(m.group(1), m.group(2))

# d. str2 with spaces changed to underscore

print(re.sub('\s', '_', str2))
print()

# e. str2 with the ellipsis (...) removed

print (re.sub('\.', '', str2))

print()


# 4. Use regex to print only floating point numbers with 2 digit
# after the decimal point in str3
str3 = "3.15; 2.383 and 11.039*2.77  1257.11"

m = re.findall('\d+\.\d{2}\\b', str3)

print(m)
"""
"""
# 5. Write a loop that asks the user input for a birth date. 
# Keep asking until you get a valid birth date.

# Validate the user input with the following steps:
# a. check that the format of str4 is valid: yyyy-mm-dd

# b. check that the month is 1-12, day is valid for the 
# month (28, 30, or 31), and the year is between 1900 and 2100

# c. then print the date as mm/dd/yyyy

"""
