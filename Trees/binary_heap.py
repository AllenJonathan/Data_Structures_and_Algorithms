# Binary Heap Property
# -> the children node have less priority than the parent nodes (MaxHeap)

# -- Info --
# -> priority in this implementation is represented by numbers.
# -> Bigger the number higher the priority
# -> Implemented using arrays

class MaxBinaryHeap:

    def __init__(self):
        self.heap = [0]
        self.length = 0

    # Time Complexity O(logN)
    def insert(self, value):
        """insert a new node"""
        self.heap.append(value)
        self.length += 1
        self._shift_up(self.length)

    def _shift_up(self, index):
        """shifts the given index node up until it achieves heap property"""
        i = index # new node index
        j = i//2 # parent index
        while i > 1 and self.heap[i] > self.heap[j]:
            self._switch(i,j)
            i = i//2 # new node goes to parent postion
            j = i//2 # parent postion is update

    def _shift_down(self):
        """shifts down the node from the top till it achieves heap property"""
        i = 1
        left = 2*i
        right = left + 1
        left_flag, right_flag = False, False
        while i <= self.length and left <= self.length and right <= self.length:
            # check which child is larger
            if self.heap[left] > self.heap[right]:
                left_flag = True
            else:
                right_flag = True
            # switch with the larger child
            if left_flag and self.heap[i] < self.heap[left]:
                self._switch(i,left)
                i = 2*i
                left = 2*i
                right = left + 1
                continue
            elif right_flag and self.heap[i] < self.heap[right]:
                self._switch(i,right)
                i = 2*i + 1
                left = 2*i
                right = left + 1
                continue
            break

    def _switch(self,i,j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    # Time Complexity O(logN)
    def extract_max(self):
        self._switch(1,self.length) # switching first and last node
        max = self.heap.pop()
        self.length -= 1
        self._shift_down()
        return max

    def print(self):
        print(self.heap)

    # Time Complexity O(logN)
    def delete(self, index):
        # 1-based indexing
        self.heap[index] = self.heap[1] + 1
        self._shift_up(index)
        self.extract_max()


# --- Comment these out --- #

# # New Max Binary Heap
# heap = MaxBinaryHeap()
#
# # insert
# heap.insert(3)
# heap.insert(7)
# heap.insert(16)
# heap.insert(76)
# heap.insert(4)
# heap.insert(99)
# heap.insert(65)
#
# # extract_max
# maximum = heap.extract_max()
# print(maximum)
# heap.print()
#
# print("________________________")
#
# # delete
# heap.delete(5)
# heap.print()
# heap.delete(3)
# heap.print()
