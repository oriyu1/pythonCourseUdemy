# %%
# Strings

"Don't do that" # to write don't do that
'She said "I want this" ' # writing quotation
print('She said "don\'t push that here"')
"Hello, " + "Nick"
"This costs " + str(6) + " dollars"
"This costs " + str(5+6) + " dollars"
"Hello:Nick".split(":")
"My nams is " + "Hello:Nick:World".split(":")[1]
# %%
# Boolean
# True and False with capittal letter
print(5==5)
print(5==4)
print(5 is 5)
print(5 is not 5)
print("This" is "This")
print(True is True)
print("True" is True) # This False because it checks not only the value but the type also


# Difference between "is" and "==" -> https://www.geeksforgeeks.org/difference-operator-python/
# %%
#Lists

print("I like " + ["Movies", "Games", "Python"][2])
print("I like " + ["Movies", 16, "Python"][1]) # will not work, can't concatanate string and integer
print("I like " + ["Movies", "16", "Python"][1])

# %%
# Dictionaries
# Basically these similars to json object in JavaScript

{'age': 27, 'hobby': 'code', 'name': 'Nick'}
{'age': 27, 'hobby': 'code', 'name': 'Nick'}["name"]

# %%
# Function
# According to PEP guide, function will be written in "Snake case" (Camel case for Classes)

# Simple
def my_function():
    print("This is my function!")
    print("A second string.")

my_function()


# Arguments
def my_function(str1, str2):
    print(str1)
    print(str2)


# my_function() without arguments, its error
my_function("This is argument 1", "This is the second argument")


def print_something(name, age):
    #print("my name is " + name + " and my age is " + str(age))
    print("my name is", name, "and my age is", age) # better way

print_something("Nick", 27)


# %%
# Now with default argument

def print_something(name = "Someone", age = "Unknown"):
    print("my name is", name, "and my age is", age) # better way

print_something("Nick")
# %%
# Now with Keyword arguments
# Lets assume I want to send only age

def print_something(name = "Someone", age = "Unknown"):
    print("my name is", name, "and my age is", age) # better way


# Lets assume I want to send only age
print_something(27) # This won't work, it will deliver it to first argument
print_something(None, "Nick") # also won't work
print_something(age = 27) # This will work
print_something(age = 27, name = "Nick") # Also work even though the order changed

# %%
# A flexible number of arguments
'''
We have function to print people but we don't know how many arguments (people) will be
We put * that means that this argument is gonna be array (List) of all the 
arguments were passed into the function
'''

def print_people(*people):
    for person in people:
        print("This person is", person)

print_people("Nick", "Dan", "Jack")
print_people("Nick", "Dan", "Jack", "King", "Smiley")
# %%
# Return values from functions

def do_math(num1, num2):
    return num1 + num2

math1 = do_math(5, 7)
math2 = do_math(11, 34)

print("First sum is", math1, "and the second sum is", math2)
# %%
# Import module and the regex module

import re
string = "'I AM NOT YELLING', she said. Tough we knew it to not be true."

# rules in regex are in []
newCapi = re.sub('[A-Z]', '', string) # replae any capital letter with nothing
newSmal = re.sub('[a-z]', '', string) # same with small letters
newSpe = re.sub('[.,\']', '', string) # remove specail characters (\ is for the ' character)
newMix = re.sub('[.,\'a-zA-Z]', '', string) # altogether but space character still there
newAll = re.sub('[.,\'A-Z+" "]', '', string) # also space ans leave small letters to see it


print(string)
print(newCapi)
print(newSmal)
print(newSpe)
print(newMix)
print(newAll)

# Now we add numbers

string = string + "6 298 - 345"
print(string)
new = re.sub('[^0-9]', '', string) # replace everything that is not a number
print(new)