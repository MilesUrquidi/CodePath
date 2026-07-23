"""
One of the drawbacks of a linked list is that it's difficult to go backwards because each Node only knows about the Node in front of it. (E.g., A -> B -> C)

A doubly linked list solves this problem! Instead of just having a next attribute, a doubly linked list also has a prev attribute that points to the Node before it. (E.g., A <-> B <-> C)

Update the Node constructor below so that the code creates a doubly linked list with head <-> tail.
"""
class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

head = Node("Isabelle")
tail = Node("K.K. Slider")

head.next = tail
tail.prev = head

print(head.value, "<->", head.next.value)
print(tail.prev.value, "<->", tail.value)