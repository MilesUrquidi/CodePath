"""
You want to add a creative twist to your posts by reversing the order of characters in each word 
within your post while still preserving whitespace and the initial word order. Given a string post, 
use a queue to reverse the order of characters in each word within the sentence.

def edit_post(post):
  pass
Example Usage:

print(edit_post("Boost your engagement with these tips")) 
print(edit_post("Check out my latest vlog")) 
Example Output:

tsooB ruoy tnemegegna htiw esehT spit
kcehC tuo ym tseval golv
✨ AI Hint: Queues


U:we need to reverse a word, and make sure the spaces are kept and everything is perserved
Input: string
output: reversed string
constrains: must use a queue
edge cases: string is empty

P: make a queue, and loop through the string until theres a space, then once theres a space, you pop the queue until its empty,
"""
from collections import deque

def edit_post(post):
    queue = deque()
    output = []
    word = []

    for ch in post:
        if ch != " ":
            queue.append(ch)
        else:
            # drain the queue into result — but how do you reverse it here?
            # then add the space
            while queue:
                word.insert(0, queue.popleft())
                output.append(word)
            output.append(" ")
            
    
    # don't forget the last word (no trailing space to trigger the drain)
    while queue:
            word.insert(0, queue.popleft())
            output.append(word)

    return " ".join(output)


print(edit_post("Boost your engagement with these tips")) 
print(edit_post("Check out my latest vlog")) 