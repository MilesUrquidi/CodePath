"""
Write a function merge_alternately() that accepts two strings word1 and word2. 
Merge the strings by adding letters in alternating order, starting with word1. 
If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

def merge_alternately(word1, word2):
    pass
Example Usage

word1 = "wol"
word2 = "oze"
merge_alternately(word1, word2)

word1 = "hfa"
word2 = "eflump"
merge_alternately(word1, word2)

word1 = "eyre"
word2 = "eo"
merge_alternately(word1, word2)
Example Output:

"woozle"
"heffalump"
"eeyore"

U: make a string that alternatively takes the first letter or each word until theyre both empty, start with word 1
P: make an empty string, then im guessing we while loop here, take out the first element of word1 then append to the string, do the same with word 2 until both strings are empty, 
then return the string
"""