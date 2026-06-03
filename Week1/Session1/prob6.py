"""
Write a function squared() that accepts a list of integers numbers as a parameter and squares each item in the list. Return the squared list.

def squared(numbers):
	pass
Example Usage

numbers = [1, 2, 3]
squared(numbers)
Example Output:

[1, 4, 9]
"""

def squared(numbers):
    for i in range(len(numbers)):
        numbers[i] = numbers[i] * numbers[i]
    print(numbers)

numbers = [1, 2, 3]
squared(numbers)