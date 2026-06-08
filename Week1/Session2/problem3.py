"""
Pooh is eating all of his hunny jars in order of smallest to largest.
Given a list of integers hunny_jar_sizes, write a function delete_minimum_elements() that continuously
removes the minimum element until the list is empty. Return a new list of the elements of hunny_jar_sizes in the order in which they were removed.

def delete_minimum_elements(hunny_jar_sizes):
	pass
Example Usage

hunny_jar_sizes = [5, 3, 2, 4, 1]
delete_minimum_elements(hunny_jar_sizes)

hunny_jar_sizes = [5, 2, 1, 8, 2]
delete_minimum_elements(hunny_jar_sizes)
Example Output:

[1, 2, 3, 4, 5]
[1, 2, 2, 5, 8]
💡Hint: While Loops

U: function that takes out the smallest number from a list until its empty, 
than have it be added to a new list that keeps track of the min that was removed. then return that list
P: make an empty list, loop through hunny jars then find the min and take it out and append it to that empty list, once hunny jars is empty return the other list
"""

def delete_minimum_elements(hunny_jar_sizes):
    res = []
    while hunny_jar_sizes:
        mini = min(hunny_jar_sizes)
        hunny_jar_sizes.remove(mini)
        res.append(mini)
    print(res)


hunny_jar_sizes = [5, 3, 2, 4, 1]
delete_minimum_elements(hunny_jar_sizes)

hunny_jar_sizes = [5, 2, 1, 8, 2]
delete_minimum_elements(hunny_jar_sizes)