def knapsack_recursive(capacity, weights, values, n):
  # Base Case: No items left or no capacity left
  if capacity == 0 or n == 0:
    return 0
  
  # If weight of the nth item (index n-1) is more than capacity,
  # then this item cannot be included in the optimal solution.
  if weights[n-1] > capacity:
    return knapsack_recursive(capacity, weights, values, n-1)

  else:
    included_value = values[n-1] + knapsack_recursive(capacity- weights[n-1], weights, values, n-1)
    execulded_value = knapsack_recursive(capacity- weights[n-1], weights, values, n-1)
  # Return the maximum of two cases:
  # 1. nth item included
  # 2. not included
  
    # Value if item n-1 is included
  
    # Value if item n-1 is not included
  return max(included_value, execulded_value)
  
  
# Example usage:
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
n = len(values)
print(f"Maximum value (Recursive): {knapsack_recursive(capacity, weights, values, n)}")
# Output should be 220