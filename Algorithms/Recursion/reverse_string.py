# Function to reverse a string with recursion and iteration.

# Recursion
def reverse_string_recursion(string):

    def reverse_recursive(string_list):
        if len(string_list) == 0:
            return "".join(reversed_list)
        reversed_list.append(string_list.pop())
        return reverse_recursive(string_list)

    string_list = list(string)
    reversed_list = []
    return reverse_recursive(string_list)

# Iteration
def reverse_string_iteration(string):
    reversed_list = []
    for i in range(len(string)-1,-1,-1):
        reversed_list.append(string[i])
    return "".join(reversed_list)


# -- Comment these out -- #

print(reverse_string_recursion('archer'))
print(reverse_string_recursion('goblin'))
print(reverse_string_recursion('giant'))

print(reverse_string_iteration('archer'))
print(reverse_string_iteration('goblin'))
print(reverse_string_iteration('giant'))
