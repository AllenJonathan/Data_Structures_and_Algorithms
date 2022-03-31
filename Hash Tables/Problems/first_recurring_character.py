# function that returns the first recurring number

# Given an array -> [2,5,4,6,2,7,9,0,7,1]
# Should return -> 2

# Approch 1 - Using Array only | Time complexity = O(n)
def first_recurring_character(array):
    existing_char = []
    for char in array:
        if not char in existing_char:
            existing_char.append(char)
        else:
            return char
    return None

# array_1 = [2,5,4,6,2,7,9,0,7,1]
# answer = first_recurring_character(array_1)
# print(answer)

# Approch 2 - Using Hash Table | Time complexity = O(n)
def first_recurring_character_2(array):
    map = {}
    for char in array:
        if char not in map:
            map[char] = 0
        else:
            return char
    return None

# array_2 = [2,5,4,6,2,7,9,0,7,1]
# answer = first_recurring_character_2(array_2)
# print(answer)
