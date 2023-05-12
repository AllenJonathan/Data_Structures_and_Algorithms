# Binary search - Linear
# Warning - works only in a sorted array

# A good explanation would be searching for a page in a book. Suppose we have to find page 287 in a 1000 page book.
# Step 1 - Split the book into two half at page 500. Since 287 is smaller we exclude pages [500 to 1000]
# Step 2 - Again split the book into half now at 250. Since 287 > 250 we exclude pages [0 to 250]
# Step 3 - Repeat the same until we exclude and are left with only the exact page

# Time complexity -> O(log(N))

array = [1, 3, 7, 9, 14, 17, 22, 29, 33, 36, 45, 47, 55, 67, 68, 77, 79, 80, 84, 99]


def binary_search(arr, value):
    low = 0
    high = len(arr) - 1
    while low <= high:
        i = low + ((high - low) // 2)
        x = arr[i]
        print(x)
        if value == x:
            return True
        elif value < x:
            high = i - 1
        elif value > x:
            low = i + 1
    return False


print(binary_search(array, 85))
