class Node:

    def __init__(self, value):
        self.value = value
        self.children = {}
        self.is_end = False

    def __str__(self):
        return self.value


# Trie is an efficient retrieval data structure where each node represents a
# character.


class Trie:

    def __init__(self):
        self.root = Node('0')

    # Time Complexity O(n) -> where n is the length of the word
    def insert(self, string):
        """inserts the word in trie"""
        current = self.root
        for char in string:
            if not char in current.children:
                current.children[char] = Node(char)
                current = current.children[char]
            else:
                current = current.children[char]
        current.is_end = True

    # Time Complexity O(n) -> where n is the length of the word
    def search(self, string):
        """searches if the given word is present in trie"""
        current = self.root
        for char in string:
            if not char in current.children:
                return False
            current = current.children[char]
        return current.is_end


# --- Comment these out --- #

# # New Trie
# trie = Trie()
#
# # insert
# names = ['ronaldo',
#     'neymar',
#     'messi',
#     'salah',
#     'benzema',
#     'modric',
#     'lewan',
#     ]
#
# for name in names:
#     trie.insert(name)
#
# # search
# print(trie.search('ronaldo'))
# print(trie.search('nemar'))
# print(trie.search('messi'))
# print(trie.search('salah'))
# print(trie.search('sala'))
# print(trie.search('ron'))
# print(trie.search('mar'))
# print(trie.search('ss'))
