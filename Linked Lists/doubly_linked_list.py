class Node:
    """ Represents one node of a linked list"""

    def __init__(self, value, previous, next):
        self.value = value
        self.previous = previous
        self.next = next

class LinkedList:
    """Doubly Linked List Implementation"""

    def __init__(self, value):
        self.head = Node(value, None, None)
        self.tail = self.head
        self.length = 1

    # Time complexity = O(1)
    def prepend(self, value):
        """insert item at index 0"""
        new_node = Node(value, None, self.head)
        self.head.previous = new_node
        self.head = new_node
        self.length += 1

    # Time complexity = O(1)
    def append(self, value):
        """insert item to end of linked list"""
        self.tail.next = Node(value, self.tail, None)
        self.tail = self.tail.next
        self.length += 1

    # Used in insert and delete to travese to index
    def _traverse_to_index(self, index):
        """traverses to find the node at the given index"""
        i = 0
        current = self.head
        while i < index-1:
            current = current.next
            i += 1
        return current

    # Time complexity = O(n)
    def insert(self, index, value):
        """insert item to given index"""
        # if index out of bounds -> append instead of insert (optional)
        if index >= self.length:
            self.append(value)
        else:
            current = self._traverse_to_index(index)
            new_node = Node(value, current, current.next)
            after_new_node = current.next
            after_new_node.prvious = new_node
            current.next = new_node
            self.length += 1

    # Time complexity = O(n)
    def delete(self, index):
        """delete item at given index"""
        current = self._traverse_to_index(index)
        unwanted_node = current.next
        current.next = unwanted_node.next
        after_unwanted_node = unwanted_node.next
        after_unwanted_node.previous = current
        del unwanted_node
        self.length -= 1

    # Time complexity = O(n) | (just for visulization)
    def print(self):
        """prints linked list"""
        print("Head:",self.head.value, "|","Tail:",self.tail.value)
        print(None, "<-- ", end="")
        current = self.head
        while current.next != None:
            print(current.value,"<--> ", end="")
            current = current.next
        print(current.value, "-->",None)


# --- Comment these out --- #

# # Creating new linked list
# linked_list = LinkedList(10)
#
# # Prepending items
# linked_list.prepend(15)
# linked_list.prepend(20)
# linked_list.prepend(25)
# linked_list.prepend(45)
#
# # Appending items
# linked_list.append(1)
# linked_list.append(2)
# linked_list.append(3)
#
# # Printing linked list
# linked_list.print()
#
# # Insert
# linked_list.insert(2,100)
# linked_list.insert(100,5)
# linked_list.print()
#
# # Delete
# linked_list.delete(2)
# linked_list.print()
