# Find factorial of a given number.

# n = 5
# 5! = 5*4*3*2*1 = 120

# There are two approaches to solve this problem.
# 1. Iteration
# 2. Recursion


# Iteration - using for loop -- Time complexity = O(n)
def find_factorial_iterative(n):
    ans = 1
    for i in range(n,1,-1):
        ans *= i
    return ans

# Recursion -- Time complexity = O(n)
def find_factorial_recursive(n):
    if n == 2:
        return 2
    return n * find_factorial_recursive(n-1)


# -- Comment these out -- #

# print(find_factorial_iterative(5))
# print(find_factorial_recursive(5))
#
# print("-----")
#
# print(find_factorial_iterative(7))
# print(find_factorial_recursive(7))
