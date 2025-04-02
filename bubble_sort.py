# Bubble Sort:
# Repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.
# Simple to implement but inefficient

def bubble_sort(mlist):
    n = len(mlist)
    for i in range(n):
        for j in range(0, n-i-1):
            if mlist[j] > mlist[j+1] :
                mlist[j], mlist[j+1] = mlist[j+1], mlist[j]
                



my_list = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(my_list)
print("Sorted array:", my_list)