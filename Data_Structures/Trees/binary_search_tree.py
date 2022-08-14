# Binary Tree Properties
# -> Nodes double after each level
# -> Number of nodes in current level = sum of all previous level node + 1

# ------------------------------------------------------------------------------

# Types of binary Trees

# -> Perfect binary tree -> Nodes at all levels are full
# Example:       7
#           4        15
#         1   5    9   20

# -> Full binary tree -> All nodes have two children or no children
# Example:       11
#           6         15
#       1      9
#            8  10

# ------------------------------------------------------------------------------

# Binary Trees must ideally be balanced (full or perfect binary tree) for
# operations to remain O(logN) if not, they will become more of like a linked
# list and oprations become O(n) which is not we need.

# A Binary Search Tree (BST) is a type of binary tree which is good at searching


class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySeachTree:

    def __init__(self):
        self.root = None

    # Time Complexity O(logN)
    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
        else:
            current_node = self.root
            while True:
                if value < current_node.value:
                    # left side
                    if current_node.left:
                        current_node = current_node.left
                    else:
                        current_node.left = new_node
                        break
                else:
                    if current_node.right:
                        # right side
                        current_node = current_node.right
                    else:
                        current_node.right = new_node
                        break

    # Time Complexity O(logN)
    def lookup(self, value):
        if not self.root:
            return False
        current = self.root
        while current:
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                return value, True
        return value, False

    # Time Complexity O(logN)
    def remove(self, value):
        # if no nodes exists
        if not self.root:
            return "No nodes exist in tree."
        current_node = self.root
        parent_node = None
        # find the node that should be removed
        while current_node:
            if value < current_node.value:
                parent_node = current_node
                current_node = current_node.left
            elif value > current_node.value:
                parent_node = current_node
                current_node = current_node.right
            # node to be removed found
            elif value == current_node.value:
                # Case 1 -> No right child
                if not current_node.right:
                    # if current is the root node
                    if not parent_node:
                        self.root = current_node.left
                    # if remove node is left of its parent
                    elif current_node.value < parent_node.value:
                        parent_node.left = current_node.left
                    # if remove node is right of its parent
                    elif current_node.value > parent_node.value:
                        parent_node.right = current_node.left
                # Case 2 -> right child that doesn't have a left child
                elif current_node.right and not current_node.right.left:
                    # if current is the root node
                    if not parent_node:
                        current_node.right.left = self.root.left
                        self.root = current_node.right
                    # if remove node is left of its parent
                    elif current_node.value < parent_node.value:
                        current_node.right.left = current_node.left
                        parent_node.left = current_node.right
                    # if remove node is right of its parent
                    elif current_node.value > parent_node.value:
                        current_node.right.left = current_node.left
                        parent_node.right = current_node.right
                # Case 3 -> right child with a left child
                elif current_node.right and current_node.right.left:
                    # find replacing node
                    replace = current_node.right.left
                    replace_parent = current_node.right
                    while replace.left:
                        replace_parent = replace
                        replace = replace.left
                    # replacng parent node's left node to replacing node's right node
                    replace_parent.left = replace.right
                    # replace removed node
                    replace.left = current_node.left
                    replace.right = current_node.right
                    # Connect to parent node if any
                    if not parent_node:
                        self.root = replace
                    elif replace.value < parent_node.value:
                        parent_node.left = replace
                    elif replace.value > parent_node.value:
                        parent_node.right = replace
                return "Removed " + str(value)
        return "Node " + str(value) + " Not Found"

    # Time Complexity O(n)
    def print(self, current=None):
        """prints all nodes of the binary search tree"""
        if not current:
            current = self.root
        if current.left:
            self.print(current=current.left)
        print(current.value, end=' ')
        if current.right:
            self.print(current=current.right)


# --- Comment these out --- #

# # New Binary Seach Tree
# bst = BinarySeachTree()
#
# # insert
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
# # lookup
# print(bst.lookup(1))
# print(bst.lookup(6))
# print(bst.lookup(15))
# print(bst.lookup(30))
# print(bst.lookup(5))
#
# # resulting binary tree
# #               9
# #        4             20
# #     1    6      15      170
# #               14       30 500
#
# bst.remove(9)
#
# # resulting binary tree
# #               14
# #        4             20
# #     1    6      15      170
# #                       30   500
#
# bst.remove(4)
#
# # resulting binary tree
# #               14
# #        6             20
# #     1           15      170
# #                       30  500
#
# bst.remove(6)
#
# # resulting binary tree
# #               14
# #        1             20
# #                 15      170
# #                       30  500
#
# bst.print()
