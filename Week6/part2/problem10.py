"""
Write a function print_reverse() that takes in the tail of a doubly linked list as a parameter.

It should print out the values of the linked list in reverse order, each separated by a space.
"""
class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

def print_reverse(tail):
    current = tail
    output = ""
    while current:
        output += f"{current.value} "
        current = current.prev
    print (output)

isabelle = Node("Isabelle")
kk_slider = Node("K.K. Slider")
saharah = Node("Saharah")
isabelle.next = kk_slider
kk_slider.next = saharah
saharah.prev = kk_slider
kk_slider.prev = isabelle

# Linked List: Isabelle <-> K.K. Slider <-> Saharah
print_reverse(saharah)