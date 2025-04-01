# Basic Searching

# Linear Search:
# This algorithm sequentially checks each element in a list until the target element is found or the list is exhausted.
# It's simple but inefficient for large datasets.

def linear_search(arr, v):
    for i  in range(len(arr)):
        if arr[i] == v:
            return i
    return -1

l = [10, 5, 2, 8, 1, 3]
v = 6
res = linear_search(l, v)

if res != -1:
    print(f"Element {v} found at {res}")
else:
    print(f"Element {v} not found")