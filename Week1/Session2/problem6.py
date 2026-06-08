"""
Given an array of strings words and a string s, implement a function is_acronym() that returns True if s is an acronym of words and returns False otherwise.

The string s is considered an acronym of words if it can be formed by concatenating 
the first character of each string in words in order. For example, "pb" can be formed from ["pooh"", "bear"], but it can't be formed from ["bear", "pooh"].

def is_acronym(words, s):
    pass
Example Usage

words = ["christopher", "robin", "milne"]
s = "crm"
is_acronym(words, s)
Example Output:

True

U: have a function that checks the first letter of words in order to see if they count as an acronym, 
it must be only the first letter and in the correct order to count as a acronym
P:have a string that tracks the first letters of the strings in the list, then do a while for the words list and see what the first letter of each word is, then add it to that string,
 then once its finished with all the words compare that string with the s and if theyre the same its true 
"""

def is_acronym(words, s):
    compare = ""
    for i in words:
        letter = i[0]
        compare += letter
    if compare == s:
        print(True)
    else:
        print(False)

words = ["christopher", "robin", "milne"]
s = "crm"
is_acronym(words, s)