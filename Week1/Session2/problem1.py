"""
Write a function reverse_sentence() that takes in a string sentence and returns the sentence with the order of the words reversed.
 The sentence will contain only alphabetic characters and spaces to separate the words. 
 If there is only one word in the sentence, the function should return the original string.

def reverse_sentence(sentence):
    pass
Example Usage:

sentence = "tubby little cubby all stuffed with fluff"
reverse_sentence(sentence)

sentence = "Pooh"
reverse_sentence(sentence)
Example Output:

"fluff with stuffed all cubby little tubby"
"Pooh"
💡Hint: String Methods

U: make a function that reverse a sentence in the oder of words, not just reverseing everything. 
P: maybe enumerate the sentence if possible? then find a way to remake the sentence with the order of words reversed. first check if its 0 or has only one word you just print the same sentence.
"""

def reverse_sentence(sentence):
    split = sentence.split()
    new = split[::-1]
    res = ' '.join(new)
    print(res)


sentence = "tubby little cubby all stuffed with fluff"
reverse_sentence(sentence)

sentence = "Pooh"
reverse_sentence(sentence)