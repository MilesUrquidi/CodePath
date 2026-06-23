"""
You often draft your posts and edit them before publishing.
 Given two draft strings draft1 and draft2, return true if they 
 are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will remain empty.

def post_compare(draft1, draft2):
  pass
Example Usage:

print(post_compare("ab#c", "ad#c"))
print(post_compare("ab##", "c#d#")) 
print(post_compare("a#c", "b")) 
Example Output:

True
True
False
💡 Hint: Helper Functions

"""


def post_compare(draft1, draft2):
    stack1 = []
    stack2 = []
    for ch in draft1:
        if ch != "#":
            stack1.append(ch)
        else:
            stack1.pop()
    for ch in draft2:
        if ch != "#":
            stack2.append(ch)
        else:
            stack2.pop()

    return stack1 == stack2

print(post_compare("ab#c", "ad#c"))
print(post_compare("ab##", "c#d#")) 
print(post_compare("a#c", "b")) 