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



#print a pine three with 
height = input("How tall is the tree:")

height = int(height)

space = height - 1

hashes = 1

stump_spaces = height - 1

while height != 0:
    for i in range(space):
        print(' ', end="")
    for i in range(hashes):
        print('#', end="")
        
    print()

    space -= 1
    hashes +=2
    height -=1

for i in range(stump_spaces):
    print(' ', end="")

print("#")