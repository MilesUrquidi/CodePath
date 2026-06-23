"""
You want to make sure your posts are clean and professional.
 Given a string post of lowercase and uppercase English letters, you want to remove any pairs 
 of adjacent characters where one is the lowercase version of a letter and the other is the uppercase version of the same letter. 
 Keep removing such pairs until the post is clean.

A clean post does not have two adjacent characters post[i] and post[i + 1] where:

post[i] is a lowercase letter and post[i + 1] is the same letter in uppercase or vice-versa.
Return the clean post.

Note that an empty string is also considered clean.

def clean_post(post):
  pass
Example Usage:

print(clean_post("poOost")) 
print(clean_post("abBAcC")) 
print(clean_post("s")) 
Example Output:

post

s
💡 Hint: Choosing the Right Approach
💡 Hint: Useful Built-In Methods

U:
input:a string of letters
output: letters without the pairs
constraints:we should use a stack to check the previous string added and compare it to the current string
edge cases: a string is empty, or every letter is a pair and the string is returned as empty


P:
we make a stack to track the letters, we loop through each charachter in the string
we first compare it to the top of the stack, and if theres a match, we remove that top from the stack. if they dont match, you an add that letter to the stack
use .lower() to check if a charachter equals the charachter equals the lower version of the next letter
"""


def clean_post(post):
    filtered = []

    for ch in post:
        if filtered and ch.lower() == filtered[-1].lower() and ch != filtered[-1]:
            filtered.pop()
        else:
            filtered.append(ch)
    return  "".join(filtered)


print(clean_post("poOost")) 
print(clean_post("abBAcC")) 
print(clean_post("s")) 