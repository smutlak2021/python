# Binary Search:
# This algorithm works on sorted lists. It repeatedly divides the search interval in half.
# It's much more efficient than linear search for large sorted datasets.



def binary_search(sortedList, v):
    left, right = 0, len(sortedList) -1
    while left <= right:
        mid = (left +right) // 2
        if sortedList[mid] == v:
            return mid
        elif sortedList[mid]< v:
            left = mid + 1
        else:
            right = mid - 1
    return -1




my_sorted_list = [1, 2, 5, 8, 9, 10]
target_value = 6
result = binary_search(my_sorted_list, target_value)
if result != -1:
    print(f"Element {target_value} found at index {result}")
else:
    print(f"Element {target_value} not found")