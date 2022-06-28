# Merge Sort implementation
# Time Complexity -> O(nlog(n))
# Space Complexity -> O(n) because a new array is created in merge()


def merge_sort(arr):
    l = len(arr)
    if l == 1:
        return arr
    left = merge_sort(arr[:l//2])
    right = merge_sort(arr[l//2:])
    return merge(left, right)

def merge(left, right):
    merged_arr = []
    while left and right:
        if left[0] < right[0]:
            merged_arr.append(left[0])
            del left[0]
        else:
            merged_arr.append(right[0])
            del right[0]
    while left:
        merged_arr.append(left[0])
        del left[0]
    while right:
        merged_arr.append(right[0])
        del right[0]
    return merged_arr


# -- Comment these out -- #

# arr_1 = [2, 8, 5, 3, 9, 4]
#
# sorted = merge_sort(arr_1)
# print(sorted)
#
# arr_2 = [7, 4, 3, 2, 1, 9, 6, 5, 8]
#
# sorted = merge_sort(arr_2)
# print(sorted)
