# Insertion Sort:
# Builds the final sorted array one item at a time.
# Efficient for small datasets or nearly sorted datasets.

def insertion_sort(mlist):
    for i in range(1, len(mlist)):
        key = mlist[i]
        j = i - 1
        while j >= 0 and key < mlist[j]:
            mlist[j + 1] = mlist[j]
            j-=1
        mlist[j+1] = key





my_list = [12, 11, 13, 5, 6]
insertion_sort(my_list)
print("Sorted array:", my_list)