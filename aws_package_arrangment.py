import itertools
import random
import time
import sys # To show memory usage estimate

def findIndex(arr):
    n = len(arr)
    for index in range(2, n):
        first = index-2
        second = index -1
        arr[second] = arr[first] + arr[second]
        if(arr[first]<=0):
            return first
    
    for i in range(n-2, n):
        if(arr[i]<=0):
            return i
        
    return -1



array_size = 8
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
importance = [9680, 7519, 3659, 2640, -609, -638, -2357, -4578]
n = len(importance)
max = -1
permutation_iterator = itertools.permutations(importance)
end_time = time.time()
print(f"Generated permutations {len(importance):,} integers in {end_time - start_time:.4f} seconds.")
# all_possible_rearrangements = list(permutation_iterator)
for p in permutation_iterator:
# for permutation in all_possible_rearrangements:
    arr = list(p)
    print(arr)
    v =findIndex(arr)
    if(v>max):
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