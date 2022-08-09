# Function to merge two sorted arrays into one sorted arrays

# Time Complexity = O(a+b) --> a and b are the sorted arrays
def merge_sorted_arrays(array_1,array_2):
    """merge two sorted arrays to one sorted array"""
    merged_array = []
    i = 0
    j = 0
    while (i < len(array_1) and j < len(array_2)):
        if array_1[i] <= array_2[j]:
            merged_array.append(array_1[i])
            i += 1
        else:
            merged_array.append(array_2[j])
            j += 1
    # add excess items to merged_array
    if i < len(array_1)-1:
        for k in range(i,len(array_1)):
            merged_array.append(array_1[k])
    if j < len(array_2)-1:
        for k in range(j,len(array_2)):
            merged_array.append(array_2[k])
    return merged_array

# array_1 = [0,3,4,31,33,35]
# array_2 = [4,6,30,40,45,55,77,88,99]
# merged_array = merge_sorted_arrays(array_1,array_2)
# print(merged_array)
