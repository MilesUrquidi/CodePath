"""
Write a function up_and_down() that accepts a list of integers lst as a parameter. The function should return the number 
of odd numbers minus the number of even numbers in the list.

def up_and_down(lst):
	pass
Example Usage

lst = [1, 2, 3]
up_and_down(lst)

lst = [1, 3, 5]
up_and_down(lst)

lst = [2, 4, 10, 2]
up_and_down(lst)
Example Output:

1
3
-4

U: We need to return how many more odd numbers are in the list than even, so odd - even
P: loop through the list, and have two things tracking how many times a number is odd and even, the subtract the amount
"""

def up_and_down(lst):
    i = 0
    j = 0
    for k in lst:
        if k % 2 == 0:
            i +=1
        else:
            j +=1
    res = j - i
    print(res)


lst = [1, 2, 3]
up_and_down(lst)

lst = [1, 3, 5]
up_and_down(lst)

lst = [2, 4, 10, 2]
up_and_down(lst)