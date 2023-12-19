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
        if self.head is None:
            return "Empty list"
        result = []
        node = self.head
        while node is not None:
            result.append(str(node.data))
            node = node.next_node
        return "\n".join(result)

    def sorted_insert(self, value):
        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        if self.head.data > value:
            new_node.next_node = self.head
            self.head = new_node
            return
        node = self.head
        while node.next_node is not None and node.next_node.data < value:
            node = node.next_node
        new_node.next_node = node.next_node
        node.next_node = new_node
