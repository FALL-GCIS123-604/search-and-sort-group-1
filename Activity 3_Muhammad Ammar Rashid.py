import random
import time


"""
Phase 1
"""

"""
    This function uses the insertion sort 
    way to sort a small elements in an array.
"""

    
def generate_sorted_data(size):
    
    for i in range(1, len(size)):
        key = size[i]
        j = i - 1
        while j >= 0 and key < size[j]:
            size[j + 1] = size[j]
            j -= 1
        size[j + 1] = key
    return size


small_data = [34, 7, 23, 32, 5, 62, 29, 12, 40, 8]
sorted_small_data = generate_sorted_data(small_data)
print("Small data sorted using insertion sort:", sorted_small_data)


"""
Phase 2
"""

"""
    This fuction uses the algorithm
    of binary search using recursion.
"""
def binary_search(arr, target, left, right):
    if left > right:
        return None  
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid  
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, right)  
    else:
        return binary_search(arr, target, left, mid - 1)  


sorted_small_data = [5, 7, 8, 12, 23, 29, 32, 34, 40, 62]


target_1 = 29
target_2 = 100


result_1 = binary_search(sorted_small_data, target_1, 0, len(sorted_small_data) - 1)
result_2 = binary_search(sorted_small_data, target_2, 0, len(sorted_small_data) - 1)


if result_1 is not None:
    print("Element", target_1, "is present at index", result_1, ".")
else:
    print("Element", target_1, "is not present in the array.")

if result_2 is not None:
    print("Element", target_2, "is present at index", result_2, ".")
else:
    print("Element", target_2, "is not present in the array.")


"""
Phase 3
"""

"""
   This function uses the merge sort 
   algorithm to sort large amount data in an array.
"""
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

       
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

       
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1



large_data = [55, 22, 89, 34, 67, 90, 15, 72, 39, 44] 


print("Original array:",large_data)
merge_sort(large_data)
print("sorting an array using merge sort:",large_data)



"""
Phase 4
"""

"""
This function uses the algorithm
of linear search using recursion.
"""
def recursive_linear_search(target, array, index=0):
    if index >= len(array):
        return None
    if array[index] == target:
        return index
    return recursive_linear_search(target, array, index + 1)

"""
    This fuction uses the algorithm
    of binary search using recursion.
"""
def recursive_binary_search(arr, target, left, right):
    if left > right:
        return None
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return recursive_binary_search(arr, target, mid + 1, right)
    else:
        return recursive_binary_search(arr, target, left, mid - 1)

target = 72
arr = [55, 22, 89, 34, 67, 90, 15, 72, 39, 44]

"""
Showing the time taken 
using linear search.
"""
begin = time.perf_counter()
index = recursive_linear_search(target, arr)
end = time.perf_counter()
print("Time taken in Recursive Linear Search:", end - begin, "seconds")

if index is not None:
    print("Target", arr[index], "found at index", index)
else:
    print("Target not found")

"""
Showing the time taken 
using binary search.
"""
begin = time.perf_counter()
index = recursive_binary_search(arr, target, 0, len(arr) - 1)
end = time.perf_counter()
print("Time taken in Recursive Binary Search:", end - begin, "seconds")

if index is not None:
    print("Target", arr[index], "found at index", index)
else:
    print("Target not found")
