def knapsack_recursive(capacity, weights, values, n):
  """
  Solves the 0/1 Knapsack problem using recursion.

  Args:
    capacity: The maximum weight capacity of the knapsack.
    weights: A list of weights for each item.
    values: A list of values for each item.
    n: The number of items currently being considered (from index 0 to n-1).

  Returns:
    The maximum value that can be obtained.
  """
  # Base Case: No items left or no capacity left
  if n == 0 or capacity == 0:
    return 0

  # If weight of the nth item (index n-1) is more than capacity,
  # then this item cannot be included in the optimal solution.
  if weights[n-1] > capacity:
    return knapsack_recursive(capacity, weights, values, n-1)

  # Return the maximum of two cases:
  # 1. nth item included
  # 2. not included
  else:
    # Value if item n-1 is included
    include_value = values[n-1] + knapsack_recursive(capacity - weights[n-1], weights, values, n-1)

    # Value if item n-1 is not included
    exclude_value = knapsack_recursive(capacity, weights, values, n-1)

    return max(include_value, exclude_value)

# Example usage:
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
n = len(values)
print(f"Maximum value (Recursive): {knapsack_recursive(capacity, weights, values, n)}")
# Output should be 220