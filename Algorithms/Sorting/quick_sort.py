# Quick Sort implementation
# Time Complexity | Average -> O(nlog(n)) | Worst -> O(n^2)
# Space Complexity -> O(nlog(n))


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = len(arr)-1
    current = 0
    i = 0
    while current != pivot:
        if arr[current] > arr[pivot]:
            swap(arr, current, pivot)
            current -= 1
            pivot -= 1
        current += 1
    left = quick_sort(arr[:pivot])
    right = quick_sort(arr[pivot+1:])
    return left + [arr[pivot]] + right

def swap(arr, current, pivot):
    if abs(pivot - current) == 1:
        arr[pivot], arr[current] = arr[current], arr[pivot]
    else:
        temp = arr[pivot-1]
        arr[pivot], arr[pivot-1] = arr[current], arr[pivot]
        arr[current] = temp


# -- Comment these out -- #

arr_1 = [2, 8, 5, 3, 9, 4]

sorted = quick_sort(arr_1)
print(sorted)

arr_2 = [7, 4, 3, 2, 1, 9, 6, 5, 8]

sorted = quick_sort(arr_2)
print(sorted)
