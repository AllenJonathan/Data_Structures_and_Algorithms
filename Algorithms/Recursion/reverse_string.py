# function to reverse a string with recursion and iteration.

# Recursion
def reverse_string(string):

    def reverse_recursive(string_list):
        if len(string_list) == 0:
            return reversed_list
        reversed_list.append(string_list.pop())
        return reverse_recursive(string_list)

    string_list = list(string)
    reversed_list = []
    return reverse_recursive(string_list)


# -- Comment these out -- #

# print(reverse_string('archer'))
# print(reverse_string('goblin'))
# print(reverse_string('giant'))
