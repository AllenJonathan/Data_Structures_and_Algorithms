# Dynamic Programming = (divide and conquer) + (memoization)

# Without memoization
count_1 = 0
def fibo(n):
    global count_1
    count_1 += 1
    if n < 2:
        return n
    return fibo(n-1) + fibo(n-2)

# With memoization
cache = {}
count_2 = 0

def fibo_memo(n):
    global cache
    global count_2
    count_2 += 1
    if n in cache:
        return cache[n]
    if n < 2:
        return n
    cache[n] = fibo_memo(n-1) + fibo_memo(n-2)
    return cache[n]


# # -- Comment these out --

print("Without dynamic programming:")
print("Ans:", fibo(30), "| Recursion_times:", count_1)
print("\n=========================\n\nWith dynamic programming:")
print("Ans:", fibo_memo(998), "| Recursion_times:", count_2)
