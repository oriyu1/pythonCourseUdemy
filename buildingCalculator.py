'''
This is our first project. It is simple but nice calculator.
In it we can see qhy we need global variables
We also see the usage of 'eval' function. 
We need to be careful because if someone enter the input some command, 
the 'eval' function will execute them and that can be very dangerous.
So we use refex to make sure only numbers enter the 'eval' function!
'''
import re

print("Our Magical Calculator")
print("Type 'quit' to exit\n")

previus = 0
run =True

def performMath():
    global run
    global previus
    equation = ""
    if previus == 0: 
        equation = input("Enter equation:")
    else:
        equation = input(str(previus))
    if equation == 'quit':
        print("Goodbye!")
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:()" "]', '', equation) # this for making sure only numbers will enter 'eval' function
    if previus == 0:
        previus = eval(equation) # eval suppose to know the order of mathematical operators
    else:
        previus = eval(str(previus) + equation)


while run:
    performMath()