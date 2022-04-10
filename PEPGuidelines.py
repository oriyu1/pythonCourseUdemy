import os, sys # this is bad
# these good
import os # 
import sys
from MyModule import foo, bar, foobar # a few functions or classes from the same module


# 2 lines spaced after the imports, not one!
# now classes and functions
def my_function(one, two, three, four, five, six):   # functions in snake style
    print("Hello World")

# sometimes we will seperate it into few lines for being readable - 
def my_function(one, two, 
                three, four, 
                five, six):   # so this is actually how it suppose to be
    print("Hello World")


# 2 lines to seperate between the end of functions and classes and the start of the next one
def second_function():
    print("Second function")


# The idendention is also for lists, this is exactly how it suppose to look like - 
my_list = [1, 2, 
           3, 4, 
           5, 6]

# About over usage of white spacec...
print("Hello " ) # Bad
print("Hello ") # Good
print("Hello","Hi") # Bad
print("Hello", "Hi") # Good

my_list[ 2 ] # Bad
my_list[2] # Good

x = 3 * 52 + 7 * 2 # Bad
x = 3*52 + 7*2 # Good, seperated by math priority