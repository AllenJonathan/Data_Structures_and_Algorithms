# Insertion Sort implementation
# Time complexity -> O(n^2)
# Best for nearly sorted arrays of small data


def insertion_sort(arr):
    l = len(arr)
    for i in range(1,l):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
    return arr


# -- Comment these out -- #

# arr_1 = [2, 8, 5, 3, 9, 4]
#
# sorted = insertion_sort(arr_1)
# print(sorted)
#
# arr_2 = [7, 4, 3, 2, 1, 9, 6, 5, 8]
#
# sorted = insertion_sort(arr_2)
# print(sorted)
