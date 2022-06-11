# Selection Sort implementation
# Time complexity -> O(n^2)

# Iteration
def selection_sort(arr):
    arr_len = len(arr)
    for n in range(arr_len-1):
        smallest = arr[n]
        index = n
        for i in range(n+1, arr_len):
            if arr[i] < smallest:
                smallest = arr[i]
                index = i
        arr[n], arr[index] = arr[index], arr[n]
    return arr


# -- Comment these out -- #

# arr_1 = [8, 2, 6, 4, 5]
#
# sorted = selection_sort(arr_1)
# print(sorted)
#
# arr_2 = [7, 4, 3, 2, 1, 9, 6, 5, 8]
#
# sorted = selection_sort(arr_2)
# print(sorted)
