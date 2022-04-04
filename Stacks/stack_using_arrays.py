class Stack:
    """Stack using arrays"""
    
    def __init__(self):
        self.data = []

    # Time complexity = O(1)
    def peek(self):
        last_item_index = len(self.data) - 1
        return self.data[last_item_index]

    # Time complexity = O(1)
    def push(self, value):
        self.data.append(value)

    # Time complexity = O(1)
    def pop(self):
        return self.data.pop()

    def print(self):
        print("Stack ---> ", self.data)


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
# print("POPed --->", popped_items)
#
# # Printing Stack
# my_stack.print()
