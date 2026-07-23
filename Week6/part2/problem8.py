"""
Write a function tail_to_head() that takes in the head of a linked list as a parameter and moves the tail of the linked list to the front.
"""

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def tail_to_head(head):
    current = head
    while current:
        if current.next.next is None:
            new = current.next.value
            current.next = None
            new_node = Node(new)
            new_node.next = head
            return new_node
        current = current.next


daisy = Node("Daisy")
mario = Node("Mario")
toad = Node("Toad") 
peach = Node("Peach")
daisy.next = mario
mario.next = toad
toad.next = peach

# Linked List: Daisy -> Mario -> Toad -> Peach
print_linked_list(tail_to_head(daisy))