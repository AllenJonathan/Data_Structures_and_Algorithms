class Node:
    """ Represents one node of a linked list"""

    def __init__(self, value, previous, next):
        self.value = value
        self.previous = previous
        self.next = next

class LinkedList:
    """Doubly Linked List Implementation"""

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def _create_first_node(self, value):
        self.head = Node(value, None, None)
        self.tail = self.head

    # Time complexity = O(1)
    def prepend(self, value):
        """insert item at index 0"""
        # for first item only
        if self.length == 0:
            self._create_first_node(value)
        else:
            new_node = Node(value, None, self.head)
            self.head.previous = new_node
            self.head = new_node
        self.length += 1

    # Time complexity = O(1)
    def append(self, value):
        """insert item to end of linked list"""
        # for first item only
        if self.length == 0:
            self._create_first_node(value)
        else:
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
        # --- checking cornor cases ---
        if index < 0 or index > self.length:
            raise IndexError("Index out of range.")
        elif index == self.length:
            self.append(value)
        elif index == 0:
            self.prepend(value)
        # --- main stuff ---
        else:
            current = self._traverse_to_index(index)
            new_node = Node(value, current, current.next)
            after_new_node = current.next
            after_new_node.prvious = new_node
            current.next = new_node
        self.length += 1

    def _delete_first_item(self):
        unwanted_node = self.head
        self.head = unwanted_node.next
        self.head.previous = None
        del unwanted_node

    def _delete_last_item(self):
        unwanted_node = self.tail
        self.tail = unwanted_node.previous
        self.tail.next = None
        del unwanted_node

    # Time complexity = O(n)
    def delete(self, index):
        """delete item at given index"""
        # --- checking cornor cases ---
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range.")
        elif index == 0:
            self._delete_first_item()
        elif index == self.length - 1:
            self._delete_last_item()
        # --- main stuff ---
        else:
            current = self._traverse_to_index(index)
            unwanted_node = current.next
            after_unwanted_node = unwanted_node.next
            current.next = after_unwanted_node
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
# linked_list = LinkedList()
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
# linked_list.insert(4,5)
# linked_list.print()
#
# # Delete
# linked_list.delete(2)
# linked_list.delete(0)
# linked_list.delete(6)
# linked_list.print()
