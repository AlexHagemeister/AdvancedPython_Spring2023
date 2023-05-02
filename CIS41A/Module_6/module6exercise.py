# Module 6 exercise: variable length argument list, generator 

############# Variable length argument list #################
def toScreen(n1, n2, n3) :
    print(n1, n2, n3)
    
T1 = (1, 2, 3)
L2 = [10, 12]

# 1. fix this function call
# toScreen(T1)
toScreen(*T1)

# toScreen(L2)
toScreen(0, *L2)

print()

# 2. write a function allToScreen such that the following
# function calls will run

def allToScreen (*args, **kwargs) :
    print(args)
    print(kwargs)

allToScreen()
allToScreen(T1)
allToScreen(1,2,3,4,5,6,7,8,9)
allToScreen(2, n2=10, n3=3)

print()

#############  Functions as first class objects ##################

# Given the greeting function:
def greeting(text1, text2="", text3="How are you?") :
    print(text1, text2)
    print(text3)
  
greeting("hello")     # what will be printed?

# line 1:  hello
# line 2:  How are you?


# 3. explain why each of the following lines will work or not work

fctA = greeting("hola")    # returns None
# fctA("ciao")             # can't call None('ciao')

fctB = greeting    
fctB("ciao")       # will work




# 4. Write a function called doWork has to input arguments: a function
# and a text string. doWork calls the function and passes the
# text string to the function.

def doWork (f, s) :
    f(s)

    
# call doWork and pass the function greeting and the string "aloha"
doWork(greeting, "aloha")

print()

# write a function doAnyWork that accepts a function and a 
# variable argument list. doAnyWork calls the function and 
# passes the argument list. doAnyWork returns the 
# function's return value

def doAnyWork(f, *args, **kwargs) :     # * is pack
    return (f(*args, **kwargs))         # * is unpack


# call doAnyWork
doAnyWork(greeting, "hello", "CIS 41A") 

# will this work? 
L = "hello there CIS41A".split()
doAnyWork(greeting, L)   # if this works, what does it print?  
# ['hello', 'there', 'CIS41A']
# How are you?

doAnyWork(greeting, *L)  # if this works, what does it print? 
# hello there
# CIS 41A 

# will any of the following print statements run successfully?
def add2(n1, n2=0) :
    return n1 + n2

print(doAnyWork(add2, 5))          # output: 5
print(doAnyWork(add2, 6, 7))       # output: 13
print(doAnyWork(add2, n2=8, n1=3)) # output: 11
# print(doAnyWork(add2, 1, 2, 3))  # output: Error

print()

########################### Generator ##########################

# 5. Write a generator to produce the first odd numbers betwen 1 and 50
# Will you use a generator function or generator expression?

gen = (num for num in range(1, 50, 2))

# Use the generator to produce the first 4 odd numbers.

for i in range (4) :
    print (next(gen))

print()

# if you don't know how many elements are in the generator, write code
# to print all of them

try :
    for i in range (100) :
        print(next(gen))
except StopIteration :
    print("out of numbers")

for datum in gen :
    print(datum)
    
print('\nNow trying infinite series')


# Infinite series odd number

def genI():
    
    i = 1
    while True :
        yield i
        i += 2
     

inf_odd = genI()

keepGoing = True

while keepGoing :
    print(next(inf_odd))
    var = input ('Keep going? Y/N: ')
    if var.upper() == 'N' :
        keepGoing = False
        
# What if series is finite?

keepGoing = True
try :
    while keepGoing :
         print(next(inf_odd))
         val = input('keep going? y to continue, any other key to end: ')
         if val.lower() != 'y' :
             keepGoing = False
except StopIteration :
    print ('out of numbers')
    
# 6. Write a generator, fibonacciGen, that produces the fibonacci sequence,
# where the current value is the sum of the 2 previous values.
# Will you use a generator function or generator expression?  


def fibonacciGen ():
    this_fib = 0
    next_fib = 1
    while True:
        yield this_fib
        this_fib, next_fib = next_fib, this_fib + next_fib

    
fgen = fibonacciGen()   
for i in range(10):
    print(next(fgen))

print()

# 7.  Given the following table:
T = [[1,2,3,4], 
     [11,12,13,14], 
     [21,22,23,24], 
     [31,32,33,34], 
     [41,42,43,44],
     [51,52,53,54],
     [61,62,63,64]]

# Add code below to create a generator that goes
# through each data value in the table, row by row,
# starting from the first row, and going across each 
# row

# tab_gen = (T[row][col] for row in range(len(T)) for col in range(len(T[row])))

tab_gen = (col for row in T for col in row)


# fill in the code below to print one value at 
# a time from T, until the user chooses 'n'

answer = 'y'
try: 
    while answer == 'y' :
        print(next(tab_gen))    # code to use the generator to
                                # print a value of the table T
        answer = input("Next val? y/n: ")
except StopIteration :
    print("end")
    
print()
# Write code to print all values of the table T

'''
for val in tab_gen :
    print(val)
'''

print(*gen) #will unpack gen and print individual values with space in between

# Package

"""
# when __init__.py is empty

import mypkg.mod1
mypkg.mod1.f1()

from mypkg import mod1,mod2
mod1.f1()
mod2.f2()

from mypkg.mod1 import f1
f1()
"""
"""
# when __init__.py gives direct access to mod1 and f2

import mypkg
mypkg.mod1.f1()
mypkg.f2()

from mypkg import f2
f2()
"""
"""
# when __init__.py contains fct1() that's not in a module

import mypkg
mypkg.fct1()
"""

# Wrap up loose ends: 

# re.sub() with backreference

import re

s = "one two three four five six"

# to swap first and last words
print(re.sub("(\w+)(.*)( \w+)", "\\3\\2 \\1", s))

##############

# _methodName to visually warn the user that it's a private method
# __methodName to cause a syntax error when user calls the method,
#  due to name mangling
