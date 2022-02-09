# This program was coded by Muzzammil Adamjee and completed on November 7th 2021.
# It is a program which can calculate multiplications, divisions, additions, and
# subtractions of two numbers. It first asks the user to select a mathematical
# operation, then requests two numbers from the user, which it then performs the
# selected operation with. The output verifies the selected operation, input
# numbers and the final operation in standard mathematical notation.
# After completion of a selected operation, it asks the user if they wish to
# continue, to which the user can select yes or no.

def isfloat(token):
    if token == '':
        return False
    dot = False
    minus = False
    for char in token :
        if char.isdigit() :  # allow many digits in a string
            continue
        elif char == "." :   # allow only one dot in a string
            if not dot :
                dot = True
            else :                                   
                return False
        elif char == "-" and token[0] == "-": # allow one minus in front
            if not minus :
                minus = True
            else :
                return False
        else :               # do not allow any other characters in a string
            return False
    return True

def choose_numbers():
    choosing_num1 = True
    while choosing_num1:
        num1 = input("Please enter the first number ")
        
        if isfloat(num1) == False:
            print("That is not a number, try again")
            choosing_num1 = True
        else:
            print(f"The first number is {num1}")
            choosing_num1 = False
    choosing_num2 = True
    while choosing_num2:
        num2 = input("Please enter a second number ")
        
        if isfloat(num2) == False:
            print("That is not a number, try again")
            choosing_num2 = True
        else:
            print(f"The second number is {num2}")
            choosing_num2 = False
    
    
    
    nums = [num1, num2]
    return nums
# subtraction
def subtract(nums):
    x = format(float(nums[0])-float(nums[1]))
    print(f'{nums[0]} - {nums[1]} = {x}')
# division
def divide(nums):
    if nums[1] == "0":
        print("dividing by zero is impossible")
    else:
        x = format(float(nums[0])/float(nums[1]))
        print(f'{nums[0]} / {nums[1]} = {x}')
#multiplication
def multiply(nums):
    x = format(float(nums[0])*float(nums[1]))
    print(f'{nums[0]} x {nums[1]} = {x}')
#addition
def addition(nums):
    x = format(float(nums[0])+float(nums[1]))
    print(f'{nums[0]} + {nums[1]} = {x}')
# format
def format(x):
    
    y = round(x,2)
    z = str(y).rstrip("0")
    m = z.rstrip(".")
       
    
    return m
        

print("Welcome to calculator program!")
calculating = True
while calculating:# the operation selection module
    
    crunching = True

    while crunching:
    
        print("Please choose one of the following operations:\nAddition - A\nSubtraction - S\nDivision - D\nMultiplication - M")
        choice = input()


# input verification

        if choice not in "ASDMasdm":
            print("Invalid operation, try again.")
            crunching = True
        elif choice == "a" or choice == "A":
            crunching = False
            print("You chose Addition")
            addition(choose_numbers())
        elif choice == "s" or choice == "S":
            crunching = False
            print("You chose Subtraction")
            subtract(choose_numbers())
        elif choice == "d" or choice == "D":
            crunching = False
            print("You chose Division")
            divide(choose_numbers())
        elif choice == "m" or choice == "M":
            crunching = False
            print("You chose Multiplication")
            multiply(choose_numbers())
    not_selected = True
    while not_selected:
        again = input("Do you want to continue? [Y/N] ")
        if again == "Y" or again == "y":
            calculating = True
            not_selected = False
        elif again == "N" or again == "n":
            print("Goodbye!")
            not_selected = False
            calculating = False
        else:
            not_selected = True
            calculating = True
