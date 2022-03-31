class Array:

    def __init__(self):
        self.length = 0
        self.data = {}

    # O(1)
    def get(self, index):
        return self.data[index]

    # O(1)
    def push(self, item):
        self.data[self.length] = item
        self.length += 1

    # O(1)
    def pop(self):
        last_item = self.data[self.length-1]
        del self.data[self.length-1]
        self.length -= 1
        return last_item

    # O(n)
    def delete(self, index):
        self.shift_items_forward(index)
        self.length -= 1

    # shift items for delete
    def shift_items_forward(self, index):
        for i in range(index, self.length-1):
            self.data[i] = self.data[i+1]
        del self.data[self.length-1]

    def insert(self, item, index):
        self.length += 1
        self.shift_items_backward(index)
        self.data[index] = item

    def shift_items_backward(self, index):
        for i in range(self.length-1, index, -1):
            self.data[i] = self.data[i-1]

    def print_array(self):
        print("[",end="")
        for i in range(self.length):
            print(self.data[i],end=",")
        print("]")

# # Creating array
# array_1 = Array()
#
# # Appending
# array_1.push(1)
# array_1.push(2)
# array_1.push(3)
# array_1.push(4)
# array_1.push(5)
# array_1.print_array() # -> [1,2,3,4,5,]
#
# # Deleting
# array_1.delete(2)
# array_1.delete(2)
# array_1.print_array() # -> [1,2,5,]
#
# # Pop
# last_item = array_1.pop() # last_item -> 5
# array_1.print_array() # -> [1,2,]
#
# # Creating again
# array_1.push(7)
# array_1.push(8)
# array_1.push(9)
# array_1.print_array() # -> [1,2,7,8,9,]
#
# # Inserting
# print(array_1.length)
# array_1.insert(item=4, index=2)
# array_1.print_array() # -> [1,2,4,7,8,9,]
