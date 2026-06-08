"""
In the extended universe of fictional bears, Goldilocks finds an enticing list of numbers in the Three Bears' house. 
She doesn't want to take a number that's too high or too low - she wants a number that's juuust right. 
Write a function goldilocks_approved() that takes in the list of distinct positive integers nums and returns any number
 from the list that is neither the minimum nor the maximum value in the array, or -1 if there is no such number.

Return the selected integer.

def goldilocks_approved(nums):
    pass
Example Usage

nums = [3, 2, 1, 4]
goldilocks_approved(nums)

nums = [1, 2]
goldilocks_approved(nums)

nums = [2, 1, 3]
goldilocks_approved(nums)
Example Output:

2
-1
2

U: have a function return a number thats not the biggest or smallest amount, if theres no middle number or such thing have it return -1
P: loop through the list, find the min and max using the functions, then loop through the list and compare the numbers with the min and max and if its not them
have it print that number, if theres no such number have it return -1
"""
def goldilocks_approved(nums):
    mini = min(nums)
    maxi = max(nums)

    for i in nums:
        if i != mini and i != maxi:
            print(i)
            return
    print(-1)

nums = [3, 2, 1, 4]
goldilocks_approved(nums)

nums = [1, 2]
goldilocks_approved(nums)

nums = [2, 1, 3]
goldilocks_approved(nums)