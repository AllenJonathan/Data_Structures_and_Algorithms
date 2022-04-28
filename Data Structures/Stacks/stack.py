class Node:
    """Represents each item in stack"""

    def __init__(self, value, next):
        self.value = value
        self.next = next


class Stack:
    """Implementation of stack using modified Linked List"""

    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    # Time complexity = O(1)
    def peek(self):
        """Return the top most node"""
        return self.top.value

    # Time complexity = O(1)
    def push(self, value):
        """Add a node to the top of the stack"""
        new_node = Node(value, None)
        # for first node only
        if self.length < 1:
            self.top = new_node
            self.bottom = new_node
        else:
            current = self.top
            self.top = new_node
            self.top.next = current
        self.length += 1

    # Time complexity = O(1)
    def pop(self):
        """Returns and removes topmost node"""
        # if no items exist
        if not self.top:
            return None
        if self.top == self.bottom:
            self.bottom = None
        pop_node = self.top
        self.top = pop_node.next
        self.length -= 1
        return pop_node.value


    # Time complexity O(n) | (just for visualization)
    def print(self):
        """Prints the stack"""
        stack_string = ""
        if self.length > 0:
            print("Bottom:", self.bottom.value, "| Top:", self.top.value)
            current = self.top
            while current.next != None:
                stack_string = " <-- " + current.value + stack_string
                current = current.next
            stack_string = current.value + stack_string
        else:
            stack_string = "Stack is empty..."
        print(stack_string)


# --- Comment these out --- #

# # Creating new Stack
# my_stack = Stack()
#
# # Pushing items
# my_stack.push('google.com')
# my_stack.push('youtube.com')
# my_stack.push('wikipedia.com')
# my_stack.push('geeksforgeeks.com')
# my_stack.push('django.com')
# my_stack.push('instagram.com')
#
# # Peek
# topmost_item = my_stack.peek()
# print(topmost_item)
#
# # Pop
# popped_items = []
# popped_items.append(my_stack.pop())
# popped_items.append(my_stack.pop())
# print(popped_items)
#
# # Printing Stack
# my_stack.print()
