''' 
CIS 41A Fall 2022
Surajit A. Bose
Module 1 exercises
'''

from math import pi

# 1. Write code to:
# prompt for a radius
# calculate the volume of a sphere: 4/3 times pi times r cube

radius = float(input("Enter a radius: "))
volume = 4 / 3 * pi * radius ** 3

# print the output "Volume = xxxx" indented by 8 spaces, 
# with 2 digits after the decimal point
# left-justified, eight spaces before value

print(f"{'Volume =':16s}{volume:.2f}")

# Whole line indented
# print (" " * 8 + f"Volume = {volume:.2f}")
# or the whole thing in an f-string

print (f"{' ' * 8}Volume = {volume:.2f}")

# 2. Textbook review exercise R2.21
# Given the string "words" below

words = "Python programming"

# Print the first character

print(words[0])

# Print the last character
# Preferred way not covered in class
# print(words[-1])
# Class way

print(words[len(words) - 1])

# Print the middle character

print(words[len(words) // 2]) # will work perfectly for odd-length string


# Print the string in all uppercase

print(words.upper())

# Print the string with first letters in uppercase

print(words.title())