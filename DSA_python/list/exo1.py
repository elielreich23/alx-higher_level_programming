def sum_list(nums):
    sum_numb = 0
    for x in nums:
        sum_numb += x
    return sum_numb

def list_mult(items):
    first = 1
    for x in items:
        first *= x
    return first

def max_num(items):
    max = items[ 0 ]
    for a in items:
        if a > max:
            max = a
    return max

def min_num(item):
    min = item [ 0 ]
    for x in item:
        if x < min:
            min = x
    return min

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [num for num in numbers if num % 2 == 0]
print("Even numbers:", even_numbers)

number = numbers[::-1]
print(number)
print(numbers)

print(sum_list([1,2,-8]))
print(list_mult([1,2,-8]))
print(min_num([1,2,-8,0]))
print(max_num([1,2,-8, 0]))
