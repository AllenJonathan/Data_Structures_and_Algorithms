# Function that reverses a string
# 3 approaches

# Time Complexity = O(n) --> n is length of the string
def reverse_string(string):
    # check input
    if type(string) != str:
        print("Input must be a string...")
    # reverse string
    reversed_string = ''
    for i in range(len(string)-1,-1,-1):
        reversed_string += string[i]
    return reversed_string

# greet = "Hello World"
# reversed_greet = reverse_string(greet)
# print(reversed_greet)

def reverse_string_2(string):
    char_array = list(string)
    char_array.reverse()
    return "".join(char_array)

# greet = "Hello World"
# reversed_greet = reverse_string_2(greet)
# print(reversed_greet)

def reverse_string_3(string):
    return string[::-1]

# greet = "Hello World"
# reversed_greet = reverse_string_3(greet)
# print(reversed_greet)
