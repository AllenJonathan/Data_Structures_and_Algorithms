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
# DepthFirstSearch would go in the order [7,4,1,15,9,20]
