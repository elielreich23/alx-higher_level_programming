#!/usr/bin/python3
def fizzbuzz():
    for number in range(1, 101):
        if number % 5 == 0 and number % 3 == 0:
            print('FizzBuzz', end=' ')
        elif number % 3 == 0:
            print('Fizz', end=' ')
        elif number % 5 == 0:
            if number == 100:
             print('Buzz', end=' ')
            else:
             print('Buzz', end=' ')
        else:
            print('{:d}'.format(number), end=' ')

if __name__ == '__main__':
    fizzbuzz()
