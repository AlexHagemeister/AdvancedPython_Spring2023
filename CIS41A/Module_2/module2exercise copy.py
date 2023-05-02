# Module 2 exercise

'''
### If statements

# 1. Textbook R3.3  
# Find errors in the following statements

# if x > 0 then
#   print(x)
   
if x > 0:
    print(x)
   
   
# if x = 1:
#   y += 1

if x == 1:
    y += 1


# sum = 0
# xStr = input("Enter an integer value ")
# x = int(xStr)
# if xStr.isdigit():
#    sum = sum + x
# else:
#    print("Bad input")
# print(sum)

sum = 0
xStr = input("Enter an integer value: ")
if xStr.isdigit():
    x = int(xStr)
    sum = sum + x
else:
    print("Bad input")
print(sum)

letterGrade = 'F'
if grade >= 90:
   letterGrade = 'A'
# if grade >= 80:
elif grade >= 80:
   letterGrade = 'B'
# if grade >= 70:
elif grade >= 70:
   letterGrade = 'C'
# if grade >= 60:
elif grade >= 60:
   letterGrade = 'D'

'''

# 2. Textbook P3.18
# Write code that reads in a string and prints whether it contains
# only letters, only lowercase letters, only digits, starts with an uppercase letter, 
# ends with a period, contains the letter 'e' 

s = input("Enter a string: ")

if s.isalpha():
    print("'" + s + "' contains only letters")
    if s.islower():
        print("'" + s + "' contains only lowercase letters")
elif s.isdigit():
    print("'" + s + "' contains only digits")
if s[0].isupper():
    print("'" + s + "' starts with an uppercase letter")
if s.endswith("."):
    print("'" + s + "' ends with a period")
if "e" in s:
    print("'" + s + "' contains the letter e")

    
### Loops

# 3. Textbook R4.2, b and d, R4.16
# Write a loop that computes the sum of squares of numbers between 1 and 100

total = 0
for i in range(1, 101):
    total += i * i

print("sum of squares from 1 to 100:", total)

# Rewrite the loop to calculate the squares as a while loop

total = 0
i = 1
while i <= 100:
    total += i * i
    i += 1

print("sum of squares from 1 to 100:", total)


### Functions

# 4. Write a function that accepts an input argument: a size between 1 and 8.
# The function checks that the size is between 1 and 8 or return False,
# If the size is valid, the function prints the following pattern, in the 
# the corresponding input size, and returns True
# * * * 
# * * 
# *

def print_star_pattern(size):
    '''Print out a star pattern based on a given size.

    @param size number of lines to be printed, must be between 1 and 8
    @return False if size is not between 1 and 8 inclusive
    '''

    if 1 <= size <= 8:
        for row in range(size, 0, -1):
            for column in range (row):
               print("*", end = " ")
            print()
        return True
    return False

# Write the function call and print "printed" if the pattern was printed.

sizeStr = input("Enter an integer between 1 and 8 inclusive: ")
while not sizeStr.isdigit():
    print("Invalid input.")
    sizeStr = input("Enter an integer between 1 and 8 inclusive: ")
    

if print_star_pattern(int(sizeStr)):
   print("printed")


# 5. Write a function that calculates the sum of all odd digits of n,
# where n is an integer that is passed as an input argument.
# Example: if n is 32677, then the sum is 3 + 7 + 7 = 17
n = 32677

def calc_odd_sum(num):
    '''Calculate the sum of all odd digits of num.
    
    @param num an integer
    @return tuple with the number of odd digits in num and their sum
    '''
    num = abs(n)
    num_odd_digits = 0
    total = 0
    while num:
        digit = num % 10
        if digit % 2:
            num_odd_digits += 1
            total += digit
        num = num // 10
    return num_odd_digits, total

odd_digits, odd_total = calc_odd_sum(n)

print(str(odd_digits), "odd digits, total is", str(odd_total))
        

# The function returns the sum and the number of odd digits.


# Call the function above and print:  X odd digits, total is Y
# where X and Y are values calculated by the function
        

##########################################

# 6. Textbook P5.4
# Write a function called middle that accepts a string as input
# and returns a string which is the middle character if the
# length of the string is odd, and returns a string which is the
# middle 2 characters if the length of the string is even.


# Write a main function that asks the user for a string,
# calls the middle function, and prints the middle string

def middle(string):
    '''Returns the middle character(s) of an input string'''
    
    length = len(string)
    midpoint = length // 2
    if length % 2:
        middle_char = string[midpoint]
    else: 
        middle_char = string[midpoint - 1] + string[midpoint]
    return middle_char
    
def main():
    string = input("Enter a string: ")
    print(middle(string))

main()
    

# 7. Given the following printInfo function that prints 
# a student's information
def printInfo(name, major, minor, age, fulltime, GPA, location):
    print ("Name:", name, "\nMajor:", major, "\nMinor:", minor,
           "\nage:", age, "\nfulltime:", fulltime, "\nGPA", GPA,
           "\nlocation:", location)
    
# how many input arguments do we need to pass to the printInfo function?
# 7


# Change the printInfo function into a printInfo2 function,
# which is more user friendly because "name" is the only 
# required argument, and the rest are optional arguments. 

def printInfo2(name, major = "GenEd", minor = None, age = 20, fulltime = False, GPA = 4.0, location = "Cupertino"):
    print ("Name:", name, "\nMajor:", major, "\nMinor:", minor,
           "\nage:", age, "\nfulltime:", fulltime, "\nGPA", GPA,
           "\nlocation:", location)

    
# call the printInfo2 function and pass to it your name and whether
# you're a full time or part time student.


printInfo2("Surajit", fulltime = True)

# Are these function calls valid?
# printInfo2("Guido", fulltime=True, major="CS")
# printInfo2(location="Cupertino", name="Grace Hopper")
# printInfo2(age=20, "Steve") NOT VALID

