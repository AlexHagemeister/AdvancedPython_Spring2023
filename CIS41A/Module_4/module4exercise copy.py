# Module 4 exercise: Exception handling and classes and objects


############ exceptions  #############
# 1. Write code to check if the user input is valid
# and keep prompting until there is a valid input

valid_input = False
while not valid_input :
    try :
        num1 = int(input("Enter an integer: "))  # what if the user enters 2.5? 'a'?
        valid_input = True

    except ValueError :
        print ("Please enter a valid integer.\n")
    
valid_input = False
while not valid_input :
    try:
        num2 = float(input("Enter a float larger than 5: "))
        # what if the user enters 3?  'bc'?
        if num2 <= 5 :
            raise ValueError("only above 5")
        valid_input = True
    except ValueError as e:
        print(str(e))
    
print(num1, num2)

# 2. Given the following code:
with open("ex4.txt", "w") as f :
    f.write("12\n8\n2\nK\9")
    
# write code to prompt the user for a filename
# and print the sum of all data from the file to screen
# If the file can't be opened, print an error 
# message and end the program
    
input_file = input("Enter input filename: ")
try:
    with open (input_file) as infile :
        total = 0
        for line in infile:
            try:
                total += int(line)
            except ValueError :
                continue
        print("Total is:", total)
except IOError :
    print("Error opening file")

# write code to prompt the user for a filename
# filename and print data from the file to screen,
# if the file can't be opened, loop back 
# and prompt for another filename until the file 
# can be opened

valid_file_name = False
while not valid_file_name :
    try:
        input_file = input("Enter input filename: ")
        with open (input_file) as infile :
            for line in infile :
                print(line)
        valid_file_name = True
    except IOError :
        print("Cannot open file " + inputfile + ". Please try again.")
        

############# classes and objects ##############
# 1. Create a new file called person.py that contains
# a Person class. The Person object can be created 
# with a required name and an optional age, default to 0

# 2. Add code to the person class so that the following code
# can run successfully

# import the correct Person class:

from person import Person

# create aperson and print
person1 = Person("Fred")
print(person1)

person2 = Person("Wilma", 10)
print(person2)

'''
# will this code run without error?
person3 = Person(10, "Wilma")       
print(person3)
person4 = Person(age = 10, name = "Wilma") 
print(person4)
person5 = Person("Wilma", "ten")   
print(person5)

# how to catch the error?

try:
    person3 = Person(10, "Wilma")
except ValueError :
    print("invalid entry")
'''

# create bff and increment age 2 times, then print
bff = Person("Wilma")
bff.happyBday()   # print: Happy Birthday, Wilma You're 1 today
bff.happyBday()   # print: Happy Birthday, Wilma You're 2 today   
print(bff)

# who's younger?
if person1 == bff:    # compare age
    print("Same age")
elif person1 < bff:
    print(person1.getName(), "is younger")
else:
    print(bff.getName(), "is younger")

