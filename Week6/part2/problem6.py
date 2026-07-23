"""
Write a function find_min() that takes in the head of a linked list and returns the
 minimum value in the linked list. You can assume the linked list will contain only numeric values.
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

def find_min(head):
    current = head
    top = head.value
    while current:
        if current.next is not None:
            if top > current.next.value:
                top = current.next.value
        current = current.next
    return top

        

head1 = Node(5, Node(6, Node(7, Node(8))))
head2 = Node(8, Node(5, Node(6, Node(7))))

# Linked List: 5 -> 6 -> 7 -> 8
print(find_min(head1))

# Linked List: 8 -> 5 -> 6 -> 7
print(find_min(head2))