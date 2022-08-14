import os
import sys
import random

# Adds the data_structures directory to sys.path for easy importing
cwd = os.getcwd()
sys.path.append(cwd + "\data_structures")

# Importing Binary Seach Tree which was previously implemented
from Trees.binary_search_tree import BinarySeachTree
from Queues.queue import Queue


# BreadthFirstSearch - searches a tree from the left to right (sideways).
# For example in,
#                7
#           4        15
#         1   5    9   20
#
# BreadthFirstSearch would go in the order [7,4,15,1,5,9,20]


def breadth_first_search(tree, value):
    """searches for 'value' in a binary tree"""
    queue = Queue()
    queue.enqueue(tree.root)
    while queue.length > 0:
        current_node = queue.shift()
        if current_node.value == value:
            return True
        if current_node.left:
            queue.enqueue(current_node.left)
        if current_node.right:
            queue.enqueue(current_node.right)
    return False


# -- Comment these out --

# Inserting values to the Binary Search Tree
# bst = BinarySeachTree()
# bst.insert(9)
# bst.insert(4)
# bst.insert(6)
# bst.insert(20)
# bst.insert(170)
# bst.insert(15)
# bst.insert(1)
# bst.insert(30)
# bst.insert(500)
# bst.insert(14)
#
# # resulting binary tree
# #               9
# #        4             20
# #     1    6      15      170
# #               14       30 500
#
# print(breadth_first_search(bst, 20))
# print(breadth_first_search(bst, 5))
