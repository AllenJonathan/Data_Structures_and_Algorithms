# Implementing a queue using two stacks
# (not a very good idea in terms of real life scenarios, but this is just a challenge)

class CrazyQueue:
    """Queue using two Stacks"""

    def __init__(self):
        # Two Stacks
        self.first_stack = []
        self.last_stack = []

    # Time complexity = O(n)
    def enqueue(self, value):
        for i in range(len(self.first_stack)):
            self.last_stack.append(self.first_stack.pop())
        self.last_stack.append(value)

    # Time complexity = O(n)
    def dequeue(self):
        for i in range(len(self.last_stack)):
            self.first_stack.append(self.last_stack.pop())
        self.first_stack.pop()

    # Time complexity = O(1)
    def peek(self):
        if len(self.last_stack) > 0:
            return self.last_stack[0]
        if len(self.first_stack) > 0:
            return self.first_stack[len(self.first_stack)-1]
        else:
            return "Empty Queue..."

    # O(1) -> (just for visualization)
    def print(self):
        if len(self.last_stack) > 0:
            print(self.last_stack)
        else:
            print(self.first_stack)


# --- Comment these out --- #

# # New Queue
# myQueue = CrazyQueue()
#
# # peek
# myQueue.peek() # returns "Empty Queue..."
#
# # enqueue
# myQueue.enqueue('Joy')
# myQueue.enqueue('Matt')
# myQueue.enqueue('Pavel')
#
# # print and peek
# myQueue.print()
# myQueue.peek() # returns Joy
#
# # dequeue
# myQueue.dequeue()
# myQueue.dequeue()
# myQueue.dequeue()
#
# # print and peek
# myQueue.print()
# myQueue.peek() # returns "Empty Queue..."
