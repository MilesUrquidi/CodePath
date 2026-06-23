"""
As part of a new feature on your social media platform, you want to highlight post titles that are symmetrical, 
meaning they read the same forwards and backwards when ignoring spaces, punctuation, and case. 
Given a post title as a string, use a new algorithmic technique the two-pointer method to determine if the title is symmetrical.

def is_symmetrical_title(title):
  pass
Example Usage:

print(is_symmetrical_title("A Santa at NASA"))
print(is_symmetrical_title("Social Media")) 
Example Output:

True
False
💡Hint: Two Pointer Technique
"""

def is_symmetrical_title(title):
    cleaned = "".join(c.lower() for c in title if c.isalpha())
    lpointer = 0
    rpointer = len(cleaned) -1

    while lpointer < rpointer:
        if cleaned[lpointer] == cleaned[rpointer]:
            lpointer += 1
            rpointer -= 1
        else:
            return False
    return True


print(is_symmetrical_title("A Santa at NASA"))
print(is_symmetrical_title("Social Media")) 