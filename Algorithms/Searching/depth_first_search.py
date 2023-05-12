# Importing Binary Search Tree which was previously implemented
from data_structures.Trees.binary_search_tree import BinarySearchTree


# There are 3 types if depth-first-search
# For example in this tree,
#                7
#           4        15
#         1   5    9   20
#
# Inorder -> [1,4,5,7,9,15,20]
# Pre-order -> [7,4,1,5,15,9,20]
# Post-order -> [1,5,4,9,20,15,7]


def depth_first_search_inorder(tree, current=None, array=[]):
    if current is None:
        current = tree.root
    if current.left:
        depth_first_search_inorder(tree, current.left, array)
    array.append(current.value)
    if current.right:
        depth_first_search_inorder(tree, current.right, array)
    return array


def depth_first_search_preorder(tree, current=None, array=[]):
    if current is None:
        current = tree.root
    array.append(current.value)
    if current.left:
        depth_first_search_preorder(tree, current.left, array)
    if current.right:
        depth_first_search_preorder(tree, current.right, array)
    return array


def depth_first_search_postorder(tree, current=None, array=[]):
    if current is None:
        current = tree.root
    if current.left:
        depth_first_search_postorder(tree, current.left, array)
    if current.right:
        depth_first_search_postorder(tree, current.right, array)
    array.append(current.value)
    return array


# -- Comment these out --

# # Inserting values to the Binary Search Tree
# bst = BinarySearchTree()
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
