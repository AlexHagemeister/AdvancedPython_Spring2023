
# Module 3 exercises 

################# List and tuple ###################

# 1. Based on Textbook R6.3
# write a loop to copy each element of L1 to L2 ...
L1 = [1,3,5,7,8,6,4,3,0]

L2 = L1          # not a copy, just a new reference pointing to the same list
print(L2 is L1)  # True


# ... by using indexing
L2 = []
for i in range(len(L1)) :
    L2.append(L1[i])

# ... by not using index
L2 = []
for elem in L1:
    L2.append(elem)


# show how the list contents are the same
# but L1 and L2 are 2 different lists

print(L2 == L1) # True
print(L2 is L1) # False

# List 3 other ways to copy a list, without using a loop

L2 = L1.copy()
L2 = list(L1)
L2 = L1[:]

# using list comprehension

L2 = [elem for elem in L1]


#2 Based on Textbook R6.18
# Write code to remove all negative values from a list
data = [2, -8, 12, -3, 24, -9, -10, -3, 29, 94]

i = 0
while i < len(data) :
    if data[i] < 0 :
        data.pop(i)
    else :
        i += 1
        
# Use j instead of len(data) to stop Python from calculating len(data) every
# time through the loop

i = 0
j = len(data)

while i < j :
    if data[i] < 0 :
        data.pop(i)
        j -= 1
    else :
        i += 1        

# for loop will not work; won't remove consecutive negatives


# 3. Use comprehension to do the same

data = [elem for elem in data if elem >= 0]

# [data.remove(elem) for elem in data if elem < 0] will not work, can't modify in place using list comprehension


# 4. Can you remove all negatives from a tuple?
data = (2, -8, 12, -3, 24, -9, -10, -3, 29, 94)

# No, tuples are immutable


################# Dictionary ###################

# 1. Write code to store the students 'fred', 'wilma', 'barney' and their
# corresponding gpa's of 3.2, 3.6, 2.7

students = dict()
students['fred'] = 3.2
students['wilma'] = 3.6
students['barney'] = 2.7

# more compact
students = { 'fred' : 3.2, 'wilma' : 3.6, 'barney' : 2.7 }

# print the student names and their gpas
print(students)

for key in students:
    print(key, students[key])

for key, value in students.items() :
    print(key, value)
    
# print all the gpa's
print(tuple(students.values()))

# 2. Write code that counts how often each letter occurs 
# in a string
str1 = "Guido Van Rossum first came up with Python in the late 1980s."


# Deprecated ways:
D = dict()       # can also use:  D = {}
for char in str1 :
    if char.isalpha() :
        if char not in D :     # if char not in D
            D[char] = 1        # start count at 1
        else :                 # otherwise
            D[char] += 1       # increase count for char
print(D)

D1 = dict()      
for char in str1 :
    if char.isalpha() :
        D1[char] = D1.get(char, 0) + 1
print(D1)


# Good way : 

from collections import defaultdict

freq = defaultdict(int)
for char in str1 :
    if char.isalpha():
        freq[char] += 1

print(freq)



################# Data structure ###################

# 1. Based on Textbook R6.28
# Create a table of m rows and n cols and initialize with 0
m = 3
n = 4

# The long way:

table = []
for row in range(m) :
    table.append([])
    for col in range(n) :
        table[row].append(0)
        
# A shorter way:

table0 = []
for row in range(m) : 
    table0.append([0] * n)
    
# using list comprehension

table = [[0] * n for row in range (m)]


# The shortest way to loop:

table1 = [[0] * n] * m


# 2. write a function to print the table in row, column format, 
# then call the function

def printTable(t):
    for row in t:
        for col in row :
            print(col, end = ' ')
        print()

# printTable(table)
 

# what does the following print?
# Each cell is sum of row number and column number of that cell

for i in range(m):
    for j in range(n):
        table[i][j] = i + j

# printTable(table)

                        
# 3. copy table to table2

table2 = table.copy()    # shallow copy

import copy

table2 = copy.deepcopy(table)

table[0][0] = -1    # will table2 be changed?  No


# 4. fill elements of bottom row of table2 with -1's

for col in range(len(table2[-1])) :
    table2[-1][col] = -1 
    
    

printTable(table2)
print()

# and all elements of left col of table2 with 0's

for row in table2:
    row[0] = 0

printTable(table2)


# 5. We start with a dictionary of student ids (sid) and associated gpa's
d = {123:3.7, 456:3.8, 789:2.7, 120:2.8}

# create an list of sid  and a tuple of gpa from d
sids = [sid for sid in d.keys()]    # sids = list(d.keys())
gpas = (gpa for gpa in d.values())  # gpas = tuple(d.values())

# create a list of tuples (k,v) from d

dtuple = [(key, value) for key, value in d.items()]
# dtuple = list(d.items())

# How do you construct a dictionary from a list of tuples?

new_dict = dict(dtuple)

# How do you construct a dictionary from the list of id and gpa?
new_dict1 = dict(zip(sids, gpas))

################# Set ###################

# Given 2 strings:
str1 = "Guido Van Rossum first came up with Python in the late 1980s."
str2 = "Rossum released the first version of Python code (0.9.0) in February 1991."

# 1. print the set of letters that are both in str1 and in str2

import string

lett_ascii = set(string.ascii_letters)
lett1 = set(str1) & lett_ascii
lett2 = set(str2) & lett_ascii
lett3 = lett1 | lett2
print(lett3)

# 2. print the set of letters that are not in either str1 or str2

lett4 = lett_ascii - lett3
print(lett4)

# 3. print the set of non-letters that are in both strings
lett5 = (set(str1)| set(str2)) - lett_ascii
print(lett5)

################# Use of iterables ###################

# 1. How do you tell if there are duplicate elements in a list?
L = [1,2,4,5,3,2,4,2]

print(len(set(L)) == len(L)) # True if no dupes, else False

# How do you tell if there are duplicate letters in str1?

new_list = [char for char in str1 if char.isalpha()]
print(len(lett1) == len(new_list))

# 2. Textbook R8.8
# In programs, the months are often numeric values 1-12.
# Suppose you're writing a program that needs to print the
# month names (ie. January) from the month number (ie. 1), 
# which would you use: a list, tuple, set, or dictionary?

# this is the easiest to type in
monthlookup = dict(zip(range(1,13), ("January February March April May June July August September October November December".split())))
print(monthlookup[2])

# can also use a list as a look up table:
months_list = [None] + "January February March April May June July August September October November December".split()

# If you need to write a program that needs to print the
# month numbers (ie 2) from the month names (ie February), 
# which would you use?

months_dict = dict(zip(months_list, (i for i in range(13))))
print(months_dict)


################# File IO ###################
# Based on Textbook P7.9
# Write code that loops to:
# - ask the user for an input filename
# - read in lines of an input file, input.txt,
# - print the lines in reverse to output.txt file
# - print the number of lines and characters in the file
# The loop ends when the user hits the Enter key

input_file = input("Enter input filename: ")
while input_file :
    with open(input_file) as infile :
        lines = []
        total = 0
        for line in infile :
            lines.append(line.rstrip())
            total += len(line)

    with open('output.txt', 'w') as outfile :
        for line in reversed(lines) :    # lines.reverse() returns None
            outfile.write(line + '\n')
    print(len(lines), "lines,", total, "characters")
    input_file = input("Enter input filename: ")



# Write code that:
# - reads in lines of an input file, input.csv,
# - print the average of all the values in each line
import csv

total = 0
fields = 0
with open ("input.csv") as infile:
    for line in csv.reader(infile): 
        for field in line :
            if not field.isalpha() :
                total += float(field)
                fields += 1
print("Average: " + str(total / fields))
