def add_first(head, task):
    fresh_node = Node(task)
    fresh_node.next = head   # point new node at old head
    return fresh_node