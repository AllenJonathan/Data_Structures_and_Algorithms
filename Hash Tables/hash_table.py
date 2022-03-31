class HashTable:

    # Time complextiy of creating self.data = O(size) (or) O(n) | not important
    def __init__(self, size):
        self.data = [None]*size

    # Hash Function - "_" before means it shouldn't be used directly
    # Time comolexity -> O(1) ideally | but here depends on length of word -> O(a)
    def _hash(self, key):
        """ Hash Function"""
        hash = 0
        for i in range(len(key)):
            hash = (hash + ord(key[i]) * i) % len(self.data)
        return hash

    # Time complexity -> O(1) (if no collision)
    def set(self, key, value):
        """
        - Hashes the key to form an address
        - Creates a bucket if the address doesn't have one
        - Appends to the bucket if bucket exists
        """
        address = self._hash(key)
        if not self.data[address]:
            self.data[address] = []
        self.data[address].append([key, value])

    # Time complexity -> O(1) (if no collision)
    def get(self,key):
        """
        - Hashes the to get the address
        - Return None if bucket doesn't exist
        - If bucket exists then loop through the bucket to find the
          item -> [key,value]
        - Return the value
        """
        address = self._hash(key)
        current_bucket = self.data[address]
        if current_bucket:
            for item in current_bucket:
                if item[0] == key:
                    return item[1]
        return None

    # Time conplextiy -> O(size) -> O(n)
    def print_hashtable(self):
        """ Prints the Hash Table"""
        print('{ ',end="")
        for bucket in self.data:
            if bucket:
                for item in bucket:
                    print(str(item[0]) + ":" + str(item[1]), end=", ")
        print('}')
        print(self.data)

    # Time complexity -> O(n) (if not collisions)
    # (or) Time complexity -> O(n + k) (where k is items in bucket) -> O(n)
    def keys(self):
        """ Return an array of all the keys in the hashtable"""
        keys_array = []
        for bucket in self.data:
            if bucket:
                for item in bucket:
                    keys_array.append(item[0])
        return keys_array


# # Creating hash table
# hash_table = HashTable(25)
#
# # Storing items (key,value) to memory
# hash_table.set('grapes', 100)
# hash_table.set('apples', 12)
# hash_table.set('mangos', 1234)
# hash_table.set('guava', 1003)
# hash_table.set('oranges', 67)
# hash_table.set('bananas', 77)
# hash_table.set('brocolli', 776)
# hash_table.set('berries', 200)
#
# # printing hash table
# hash_table.print_hashtable()
#
# # Extracting value from hashtable
# value = hash_table.get('grapes')
# print(value)
#
# # Return keys array
# keys = hash_table.keys()
# print(keys)
