import os
import sys
import random

# Adds the data_structures directory to sys.path for easy importing
cwd = os.getcwd()
sys.path.append(cwd + "\data_structures")

# Importing Binary Seach Tree which was previously implemented
from Trees.binary_search_tree import BinarySeachTree

# There are 3 types if depth-first-search
# For example in this tree,
#                7
#           4        15
#         1   5    9   20
#
# Inorder -> [1,4,5,7,9,15,20]
# Pre-order -> [7,4,1,5,15,9,20]
# Post-order -> [1,5,4,9,20,15,7]


def depth_first_search_inorder(tree, current=None, list=[]):
    if current is None:
        current = tree.root
    if current.left:
        depth_first_search_inorder(tree, current.left, list)
    list.append(current.value)
    if current.right:
        depth_first_search_inorder(tree, current.right, list)
    return list

def depth_first_search_preorder(tree, current=None, list=[]):
    if current is None:
        current = tree.root
    list.append(current.value)
    if current.left:
        depth_first_search_preorder(tree, current.left, list)
    if current.right:
        depth_first_search_preorder(tree, current.right, list)
    return list

def depth_first_search_postorder(tree, current=None, list=[]):
    if current is None:
        current = tree.root
    if current.left:
        depth_first_search_postorder(tree, current.left, list)
    if current.right:
        depth_first_search_postorder(tree, current.right, list)
    list.append(current.value)
    return list


# -- Comment these out --

# # Inserting values to the Binary Search Tree
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
# print(depth_first_search_inorder(bst))
# print(depth_first_search_preorder(bst))
# print(depth_first_search_postorder(bst))
