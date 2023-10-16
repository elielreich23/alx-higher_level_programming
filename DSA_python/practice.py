#!/usr/bin/python3
# basic aritmetics
"""num1, num2 = input('enter two digits: ').split()
num1 = int(num1)
 num2 = int(num2)
sum = num1 + num2
diff = num1 - num2
mul = num1 * num2
div = num1 / num2

print("{} + {} = {}".format(num1, num2, sum))
 print("{} - {} = {}".format(num1, num2, diff))
print("{} * {} = {}".format(num1, num2, mul))
print("{} / {} = {}".format(num1, num2, div))"""

# recive miles and convert to km
"""miles = input('Enter miles: ')
miles = int(miles)
kilometer = miles * 1.60934
print("{} miles is equals to  kilometer".format(miles, kilometer))"""

#calculator
""" num1, num2 = input('Enter two digit: ').split()
operator = input('entre operator: ')
num1 = int(num1)
num2 = int(num2)
if operator == '+':
    print("{} + {} = {}".format(num1, num2, num1 + num2))
elif operator == '-':
    print("{} - {} = {}".format(num1, num2, num1 - num2))
elif operator == '*':
    print("{} * {} = {}".format(num1, num2, num1 * num2))
else:
    print("{} / {} = {}".format(num1, num2, num1 / num2)) """


"""for i in range(1, 101):
    if i%2 != 0:
        print(i, end=' ')
    elif i % 2 ==0:
        print('even', end=' ')"""


"""print a pine three with 
height = input("How tall is the tree:")

height = int(height)

space = height - 1

hashes = 1

stump_spaces = height - 1

while height != 0:
    for i in range(space):
        print(' ', end="")
    for i in range(hashes):
        print('*', end="")
        
    print()

    space -= 1
    hashes +=2
    height -=1

for i in range(stump_spaces):
    print(' ', end="")

print("*")"""
"""
#return a list of prime
#input maximum prime
#use for to loop through
#function to check for reminder
def prime_num(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    
    return True

#function to get prime_num list
def get_prime__num(max_num):
    prime_list = []
    for number in range(2, max_num):
        if prime_num(number):
            prime_list.append(number)
    return prime_list

#ask user to input max number to check
max_num_check = int(input("Enter the max number to check:"))
prime_list = get_prime__num(max_num_check)
for primes in prime_list:
    print(primes)"""

"""
to check for unkown number of argumets we use 
(*args) args 
"""
"""
#calculator that calculate area of differents shapes

#get_are&a func
import math
def get_area(shape):
    shape = shape.lower()
    #more shape can be created with more conditional statements and the function to calculate the shape
    if shape == "rectangle":
        rect_area()
    elif shape == "circle":
        circ_area()
    else:
        print("Enter a shape")

#func to calcuate rectangle area
def rect_area():
    lenght = float(input("Enter the lenght:"))
    width = float(input("Enter the width:"))

    area = lenght * width

    print("The area of the rectangle is: ", area)

def circ_area():
    radius = float(input("Enter the radius:"))
    
    area = math.pi * (math.pow(radius, 2))

    print("The area of the circle is {:.2f}: ".format(area)) 

#ask user for shape
def main():
    shape_type = input("Enter a shape:")

    #function to calculate area
    get_area(shape_type)
main()"""
"""
name = input("Enter your name:")
surname = input("enter your suname:")
fullname = surname + name
print(name[0].upper() + name[1:].lower() + " " + surname[0].upper() + surname[1:].lower())
reverse_name = name[::-1]
print(name[0].replace('E', 'a'))#code only pics the first letter of the word
print(reverse_name)
print (len(fullname))
#a = int(input("enter a number:\n"))
#b = int(input("enter a second number:\n"))
sum = a + b 
print("the sum of two interger is = ", sum)
"""





#same program but have some specifics
num = list(map(int , input("enter a list of number: ").split()))
target = int(input("enter the desired sum"))
seen = {}
for i, num in enumerate(num):
        complement = target - num
        if complement in seen:
                print("indices:", seen[complement], i)
                break
        seen[num] = i 
else:
        print("There are no numbers in this list that add up to the desired sum")
#friends = ["kim", "james", "peter"]
#print(friends[0] + " is my best friend, " + friends[1] +  " is my brother ")
#print(friends[0] + " is my best friend, " + friends[1] + " is my brother")
#import sys

#locate_python = sys.exec_prefix

#print(locate_python)

