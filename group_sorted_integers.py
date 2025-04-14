import collections
import bisect
import random

def group_unique_sorted_integers(nums):
    """
    Groups a list of integers into sorted ascending sublists,
    where each sublist contains unique items.

    Each group starts with the smallest currently available number.
    Subsequent numbers are added to a group if they are the smallest
    available number STRICTLY GREATER than the last number added
    to that group. Handles duplicate integers in the input by allowing
    them to start or be part of different groups.

    Args:
        nums: A list of integers (may contain duplicates).

    Returns:
        A list of lists, where each inner list is a sorted group
        containing unique items, formed according to the rules.
        Returns an empty list if the input is empty.
    """
    if not nums:
        return []

    # Use Counter to efficiently track the counts of available numbers
    counts = collections.Counter(nums)

    results = []

    # Continue processing as long as there are numbers available
    while counts:
        current_group = []
        last_added = -float('inf') # Initialize for comparison

        # Find the absolute smallest number currently available to start the group
        available_keys = sorted(counts.keys())
        if not available_keys: # Safety check if counts became empty unexpectedly
             break

        start_num = available_keys[0] # The smallest available key starts the group

        current_group.append(start_num)
        counts[start_num] -= 1
        if counts[start_num] == 0:
            del counts[start_num] # Remove number if its count drops to zero
        last_added = start_num

        # Greedily extend the current group with unique items
        while True:
            next_num_candidate = None
            found_candidate = False

            # Get currently available keys sorted
            current_available_keys = sorted(counts.keys())

            # --- Modification for Uniqueness ---
            # We need the smallest available key that is STRICTLY GREATER than last_added.
            # bisect_right finds the insertion point AFTER any existing last_added values.
            search_start_idx = bisect.bisect_right(current_available_keys, last_added)

            # Iterate through available keys starting from this index
            for i in range(search_start_idx, len(current_available_keys)):
                num = current_available_keys[i]
                # num > last_added is guaranteed by bisect_right and loop start index
                if counts[num] > 0: # Check if we actually have any left
                    next_num_candidate = num
                    found_candidate = True
                    break # Found the smallest available > last_added

            if found_candidate:
                # Add the found number (guaranteed unique in this group)
                current_group.append(next_num_candidate)
                counts[next_num_candidate] -= 1
                if counts[next_num_candidate] == 0:
                    del counts[next_num_candidate]
                last_added = next_num_candidate # Update last_added for the next iteration
            else:
                # No suitable number (> last_added) found to extend the current group
                break # Exit the inner while loop

        # Add the completed group (with unique elements) to the results
        results.append(current_group)
        # return current_group

    return results

def generate_random_list(size, min_val=0, max_val=1):
    """Generates a list of random floating-point numbers."""
    random_list = []
    for _ in range(size):
        random_list.append(random.randint(min_val, max_val))
    return random_list

# lst = generate_random_list(10**4, 1, 10000)  
# # print(f"Generated list of size: {len(lst)}")

# print(f"Output: {group_unique_sorted_integers(lst)}")
# # Expected: [[1, 2, 3, 4], [1, 2]] - Same as before, duplicates were already in different groups


# # --- Examples ---
# print(f"Input: [1, 2, 3, 1, 2, 4]")
# print(f"Output: {group_unique_sorted_integers([1, 2, 3, 1, 2, 4])}")
# # Expected: [[1, 2, 3, 4], [1, 2]] - Same as before, duplicates were already in different groups

# print("-" * 20)

# print(f"Input: [3, 1, 2, 1]")
# print(f"Output: {group_unique_sorted_integers([3, 1, 2, 1])}")
# # Expected: [[1, 2, 3], [1]] - Same as before

# print("-" * 20)

# print(f"Input: [4, 5, 1, 2, 3, 4, 1, 2]")
# print(f"Output: {group_unique_sorted_integers([4, 5, 1, 2, 3, 4, 1, 2])}")
# # Expected: [[1, 2, 3, 4, 5], [1, 2, 4]] - Still the same, the second 4 fit uniquely in the second group

# print("-" * 20)

print(f"Input: [8, 8, 9, 9, 1, 1, 2]")
print(f"Output: {group_unique_sorted_integers([8, 8, 9, 9, 1, 1, 2])}")
# Expected: [[1, 2, 8, 9], [1, 8, 9]] - Still the same

# print("-" * 20)

# # --- Example showing the difference ---
# print(f"Input: [1, 1, 1, 2, 2, 3]")
# print(f"Output: {group_unique_sorted_integers([1, 1, 1, 2, 2, 3])}")
# # Expected: [[1, 2, 3], [1, 2], [1]]
# # Why?
# # Group 1: Starts with 1. Smallest > 1 is 2. Smallest > 2 is 3. Group: [1, 2, 3]. Counts: {1: 2, 2: 1}
# # Group 2: Starts with smallest available: 1. Smallest > 1 is 2. Group: [1, 2]. Counts: {1: 1}
# # Group 3: Starts with smallest available: 1. Cannot find > 1. Group: [1]. Counts: {}

# print("-" * 20)

# print(f"Input: [5, 5, 5, 5]")
# print(f"Output: {group_unique_sorted_integers([5, 5, 5, 5])}")
# # Expected: [[5], [5], [5], [5]] - Same as before, 5 is not > 5

# print("-" * 20)

# print(f"Input: []")
# print(f"Output: {group_unique_sorted_integers([])}")
# # Expected: []