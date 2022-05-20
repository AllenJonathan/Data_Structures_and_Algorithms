# Bubble sort implementation

# Recursive bubble sort
def bubble_sort(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            bubble_sort(arr)
    return arr

def bubble_sort_iterative(arr):
    l = len(arr) - 1
    for i in range(l):
        for j in range(l):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


arr_1 = [8, 2, 6, 4, 5]

sorted = bubble_sort(arr_1)
print(sorted)

arr_2 = [8, 2, 6, 4, 5]

sorted = bubble_sort_iterative(arr_2)
print(sorted)
