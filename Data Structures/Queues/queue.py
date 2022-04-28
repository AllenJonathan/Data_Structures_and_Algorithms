class Node:
    """ Represents one node of a queue"""

    def __init__(self, value, next):
        self.value = value
        self.next = next


class Queue:

    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    # Time complexity = O(1)
    def peek(self):
        """Gets first queue element"""
        return self.first.value

    # Time complexity = O(1)
    def enqueue(self, value):
        """Adds an element to the end of a queue"""
        new_node = Node(value, None)
        # for first element
        if self.length == 0:
            self.last = new_node
            self.first = self.last
        else:
            enque_node = new_node
            self.last.next = enque_node
            self.last = enque_node
        self.length += 1

    # Time complexity = O(1)
    def dequeue(self):
        """Removes the first element in the queue"""
        if self.first == self.last:
            self.last = None
        deque_node = self.first
        self.first = deque_node.next
        del deque_node
        self.length -= 1

    # Time complexity = O(n) | (just for visualization)
    def print(self):
        if self.length == 0:
            print("Queue is empty...")
        else:
            print("FIRST| ", end="")
            current = self.first
            while current.next != None:
                print(current.value, "--- ", end="")
                current = current.next
            print(current.value, end="")
            print(" |LAST")


# --- Comment these out --- #

# # Creating new Queue
# my_queue = Queue()
#
# # Enqueue
# my_queue.enqueue('ronaldo')
# my_queue.enqueue('messi')
# my_queue.enqueue('neymar')
# my_queue.enqueue('lewandowski')
#
# # Dequeue
# my_queue.dequeue()
# my_queue.dequeue()
#
# # Printing queue
# my_queue.print()
#
# # Peek
# first_person = my_queue.peek()
# print("First person: " + first_person)
