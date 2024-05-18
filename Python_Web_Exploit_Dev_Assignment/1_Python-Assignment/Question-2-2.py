# Implement the following Searching and Sorting techniques in Python by using functions.

# ii) Binary Search 

# Answer 2

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = [10, 20, 30, 40, 50]
x = int(input("Enter the value to search: - "))
print(binary_search(arr, x))