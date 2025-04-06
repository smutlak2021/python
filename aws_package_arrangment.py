import itertools
import random
import time
import sys # To show memory usage estimate

def findIndex(arr):
    n = len(arr)
    for index in range(2, len(arr)):
        arr[index -1] = arr[index-2] + arr[index-1]
        if(arr[index-2]<=0):
            return index-2;
    
    for i in range(len(arr)-2, len(arr)):
        if(arr[i]<=0):
            return i
        
    return -1



array_size = 100
min_val = -10000
max_val = 10000

print("\n--- Using Python list ---")
start_time = time.time()

importance = [random.randint(min_val, max_val) for _ in range(array_size)]
end_time = time.time()
print(f"Generated {len(importance):,} integers in {end_time - start_time:.4f} seconds.")
# print(importance)
# importance = [2, 1, -4]
# importance = [1, 2, -6, 3]
# importance = [1, 2]
n = len(importance)
max = -1
permutation_iterator = itertools.permutations(importance)
all_possible_rearrangements = list(permutation_iterator)
arr = []
for permutation in all_possible_rearrangements:
    arr = list(permutation)
    v =findIndex(arr)
    if(v>max):
        # print(arr)
        # print(v)
        max = v

print("result=")
print(max)
end_time = time.time()
print(f"Done {len(importance):,} integers in {end_time - start_time:.4f} seconds.")



# while n>0:
#     print("***********")
#     print(importance)

#     index = findIndex(importance.copy())
#     if index > max:
#         max = index

#     item = importance.pop(0)
#     importance.append(item)
    
#     n= n-1