"""
Write a function sum_of_digits() that accepts an integer num and returns the sum of num's digits.

def sum_of_digits(num):
    pass
Example Usage

num = 423
sum_of_digits(num)

num = 4
sum_of_digits(num)
Example Output:

9 # Explanation: 4 + 2 + 3 = 9
4 

U: return the sum of all the digits in a number
P: use mods to find the rightmost number, then // which is floor division to chop that number down by one. also use while looop
"""

def sum_of_digits(num):
    total = 0
    while num:
        add = num % 10
        num = num // 10
        total += add
    print(total)


num = 423
sum_of_digits(num)

num = 4
sum_of_digits(num)