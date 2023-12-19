#!/usr/bin/python3

class Node:
    def __init__(self, data, next_node=None):
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        if next_node is not None and not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")
        self.data = data
        self.next_node = next_node

    def __repr__(self):
        return f"Node({self.data})"


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        return " -> ".join(str(node.data) for node in self)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next_node

    def sorted_insert(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        elif self.head.data > value:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next_node is not None and current_node.next_node.data < value:
                current_node = current_node.next_node
            new_node.next_node = current_node.next_node
            current_node.next_node = new_node

            list = SinglyLinkedList()
list.sorted_insert(5)
list.sorted_insert(3)
list.sorted_insert(1)
list.sorted_insert(7)
print(list) # prints: Node(1) -> Node(3) -> Node(5) -> Node(7)
