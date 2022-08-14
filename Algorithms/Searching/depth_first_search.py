import os
import sys
import random

# Adds the data_structures directory to sys.path for easy importing
cwd = os.getcwd()
sys.path.append(cwd + "\data_structures")

# Importing Binary Seach Tree which was previously implemented
from Trees.binary_search_tree import BinarySeachTree

# DepthFirstSearch - searches a tree from the up to down (downwards).
# For example in,
#                7
#           4        15
#         1   5    9   20
#
# DepthFirstSearch would go in the order [7,4,1,5,15,9,20]


def depth_first_search_recursive(current, list=[]):
    if current.left:
        depth_first_search_recursive(current.left, list)
    list.append(current.value)
    if current.right:
        depth_first_search_recursive(current.right, list)
    return list

# -- Comment these out --

# Inserting values to the Binary Search Tree
bst = BinarySeachTree()
bst.insert(9)
bst.insert(4)
bst.insert(6)
bst.insert(20)
bst.insert(170)
bst.insert(15)
bst.insert(1)
bst.insert(30)
bst.insert(500)
bst.insert(14)

# resulting binary tree
#               9
#        4             20
#     1    6      15      170
#               14       30 50
print(depth_first_search_recursive(bst.root))
