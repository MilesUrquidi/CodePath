"""
Write a function make_divisible_by_3() that accepts an integer array nums. 
In one operation, you can add or subtract 1 from any element of nums. 
Return the minimum number of operations to make all elements of nums divisible by 3.

def make_divisible_by_3(nums):
    pass
Example Usage

nums = [1, 2, 3, 4]
make_divisible_by_3(nums)

nums = [3, 6, 9]
make_divisible_by_3(nums)
Example Output:

3
0

U: check how many times you had to change a number to make it divisble by three, then return that amount
P: have a counter that checks how many numbers arent divisble by three, and check the remainder of each number from mod 3. if its 1, you subtract 1,
if its 2, you add 1, and if its zero you dont have to do anything. anytime its not 0 you must increase the counter by 1.
"""

def make_divisible_by_3(nums):
    counter = 0
    for i in nums:
        if i % 3 == 0:
            counter = counter
        else:
            counter += 1
    print(counter)
        
nums = [1, 2, 3, 4]
make_divisible_by_3(nums)

nums = [3, 6, 9]
make_divisible_by_3(nums)