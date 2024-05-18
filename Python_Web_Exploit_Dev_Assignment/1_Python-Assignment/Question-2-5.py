# Implement the following Searching and Sorting techniques in Python by using functions.

# v) Quick Sort

# Answer 5

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

arr = [80, 10, 40, 90, 20]
print(quick_sort(arr))