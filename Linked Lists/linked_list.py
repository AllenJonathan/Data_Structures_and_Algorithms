class Node:
    """ Represents one node of a linked list"""

    def __init__(self, value, next):
        self.value = value
        self.next = next

class LinkedList:
    """Singly Linked List Implementation"""

    def __init__(self, value):
        self.head = Node(value, None)
        self.tail = self.head

    # Time complexity = O(1)
    def prepend(self, value):
        """insert at index 0"""
        self.head = Node(value, self.head)

    # Time complexity = O(1)
    def append(self, value):
        self.tail.next = Node(value, None)
        self.tail = self.tail.next

    # Time complexity = O(n)
    def insert(self, index, value):
        i = 0
        current = self.head
        while i < index-1:
            current = current.next
            i += 1
        new_node = Node(value, current.next)
        current.next = new_node

    # Time complexity = O(n)
    def delete(self, index):
        i = 0
        current = self.head
        while i < index-1:
            current = current.next
            i += 1
        to_delete = current.next
        current.next = current.next.next
        del to_delete

    # Time complexity = O(n) | (just for visulization)
    def print_linked_list(self):
        print("Head: " + str(self.head.value))
        print("Tail: " + str(self.tail.value))
        current = self.head
        while current != None:
            print(current.value, "--> ", end="")
            current = current.next
        print(None)

    # def delete(self, index):


linked_list = LinkedList(10)
linked_list.prepend(15)
linked_list.prepend(20)
linked_list.prepend(25)
linked_list.prepend(45)
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.print_linked_list()
linked_list.insert(2,100)
linked_list.print_linked_list()
linked_list.delete(2)
linked_list.print_linked_list()
