# Fibonacci sequence
# First two numbers = 0,1
# The numbers following is the sum the previous two numbers

# fibo(7) = 0,1,2,3,5,8,13

# Iterative - Time complexity -> O(n)
def fibo_iterative(n):
    if n < 2:
        return n
    else:
        ans = 0
        first = 1
        second = 1
        for i in range(3,n+1):
            ans = first + second
            second = first
            first = ans
        return ans


# Recursive - Time complexity -> 2^n
def fibo_recursive(n):
    if n < 2:
        return n
    else:
        return fibo_recursive(n-1) + fibo_recursive(n-2)



print(fibo_iterative(7))
print(fibo_recursive(7))
