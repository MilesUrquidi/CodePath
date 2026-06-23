"""
On your platform, comments on posts are displayed in the order they are received. 
However, for a special feature, you need to reverse the order of comments before displaying them.
 Given a queue of comments represented as a list of strings, reverse the order using a stack.

def reverse_comments_queue(comments):
  pass
Example Usage:

print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))

print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))
Example Output:

['Thanks for sharing.', 'Love it!', 'Great post!']
['Well written.', 'Interesting read.', 'First!']
"""

def reverse_comments_queue(comments):
    stack = []
    while comments:
        stack.append(comments.pop())
    return stack
    


print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))

print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))