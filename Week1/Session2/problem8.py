"""
Given two lists lst1 and lst2, write a function exclusive_elemts() that returns a new list that contains 
the elements which are in lst1 but not in lst2 and the elements that are in lst2 but not in lst1.

def exclusive_elemts(lst1, lst2):
	pass
Example Usage

lst1 = ["pooh", "roo", "piglet"]
lst2 = ["piglet", "eeyore", "owl"]
exclusive_elemts(lst1, lst2)

lst1 = ["pooh", "roo"]
lst2 = ["piglet", "eeyore", "owl", "kanga"]
exclusive_elemts(lst1, lst2)

lst1 = ["pooh", "roo", "piglet"]
lst2 = ["pooh", "roo", "piglet"]
exclusive_elemts(lst1, lst2)
Example Output:

["pooh", "roo", "eeyore", "owl"]
["pooh", "roo", "piglet", "eeyore", "owl", "kanga"]
[]

U: make a function that returns all the unique elements(elements that only apear in one) from two lists
P: i could brute force this and check every element from both lists but i want to find a better way, i guess its fine if we loop through the whole first list and compare with the second
like check for i in list1, if i not in list 2 append it to the empty list, and do the same for list 2
"""

def exclusive_elemts(lst1, lst2):
    res = []
    for i in lst1:
        if i not in lst2:
            res.append(i)
    for i in lst2:
        if i not in lst1:
            res.append(i)
    print(res)

lst1 = ["pooh", "roo", "piglet"]
lst2 = ["piglet", "eeyore", "owl"]
exclusive_elemts(lst1, lst2)

lst1 = ["pooh", "roo"]
lst2 = ["piglet", "eeyore", "owl", "kanga"]
exclusive_elemts(lst1, lst2)

lst1 = ["pooh", "roo", "piglet"]
lst2 = ["pooh", "roo", "piglet"]
exclusive_elemts(lst1, lst2)