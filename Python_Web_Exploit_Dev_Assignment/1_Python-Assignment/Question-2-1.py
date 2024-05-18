# Implement the following Searching and Sorting techniques in Python by using functions.

# i) Linear Search 
# ii) Binary Search 
# iii) Selection Sort
# iv) Merge Sort 
# v) Quick Sort

# Answer 1

def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

arr = [10, 20, 30, 40, 50]
x = int(input("Enter the value to search: - "))
print(linear_search(arr, x))