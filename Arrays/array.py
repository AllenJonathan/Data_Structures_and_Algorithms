class Array:

    def __init__(self):
        self.length = 0
        self.data = {}

    # Time complextiy = O(1)
    def get(self, index):
        """get item using index"""
        return self.data[index]

    # Time complextiy = O(1)
    def append(self, item):
        """append item to the end of the array"""
        self.data[self.length] = item
        self.length += 1

    # Time complextiy = O(1)
    def pop(self):
        """remove last and return it"""
        last_item = self.data[self.length-1]
        del self.data[self.length-1]
        self.length -= 1
        return last_item

    # Time complextiy = O(n)
    def delete(self, index):
        """delete the item in the given index"""
        self._shift_items_forward(index)
        self.length -= 1

    # shift items for delete
    def _shift_items_forward(self, index):
        for i in range(index, self.length-1):
            self.data[i] = self.data[i+1]
        del self.data[self.length-1]

    # Time complextiy = O(n)
    def insert(self, item, index):
        """insert an item at the given index"""
        self.length += 1
        self._shift_items_backward(index)
        self.data[index] = item

    # shift items to insert
    def _shift_items_backward(self, index):
        for i in range(self.length-1, index, -1):
            self.data[i] = self.data[i-1]

    # Time complexity = O(n) | (just for visulization)
    def print_array(self):
        """prints the array"""
        print("[",end="")
        for i in range(self.length):
            print(self.data[i],end=",")
        print("]")

# # Creating array
# array_1 = Array()
#
# # Appending
# array_1.append(1)
# array_1.append(2)
# array_1.append(3)
# array_1.append(4)
# array_1.append(5)
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
# array_1.append(7)
# array_1.append(8)
# array_1.append(9)
# array_1.print_array() # -> [1,2,7,8,9,]
#
# # Inserting
# array_1.insert(item=4, index=2)
# array_1.print_array() # -> [1,2,4,7,8,9,]
