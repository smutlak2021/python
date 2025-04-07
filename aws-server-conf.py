import math
def knapsack_dp_tabulation(capacity, weights, values, n):
  """
  Solves the 0/1 Knapsack problem using Dynamic Programming (Tabulation).

  Args:
    capacity: The maximum weight capacity of the knapsack.
    weights: A list of weights for each item.
    values: A list of values for each item.
    n: The number of items.

  Returns:
    The maximum value that can be obtained.
  """
  # Create the DP table with dimensions (n+1) x (capacity+1)
  # Initialize all entries to 0
  dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

  # Fill the table row by row (item by item)
  for i in range(1, n + 1):  # i represents considering the first 'i' items
    # Get the weight and value of the current item (i-1 is the index)
    current_weight = weights[i-1]
    current_value = values[i-1]

    for curr_capacity in range(1, capacity + 1): # j represents the current capacity being considered
      # Case 1: If the current item's weight is more than the current capacity j,
      # we cannot include it. The value is the same as without this item.
      if current_weight > curr_capacity:
        dp[i][curr_capacity] = dp[i-1][curr_capacity]
      # Case 2: The current item can fit. Decide whether to include it or not.
      else:
        # Value if we DO NOT include item i
        value_exclude = dp[i-1][curr_capacity]
        # Value if we DO include item i
        value_include = current_value + dp[i-1][curr_capacity - current_weight]
        # Take the maximum of the two choices
        dp[i][curr_capacity] = max(value_exclude, value_include)

  # The final answer is in the bottom-right corner
  return dp[n][capacity]


eff = [4, 4, 6, 7]
costs = [1, 1, 2, 2]
k = 7

# eff = [75, 104, 72,72,8,125]
# costs = [1, 2, 2, 1, 2, 1]
# k = 376
n = len(costs)

largest_cost = max(costs)
digits = math.floor(math.log10(largest_cost) + 1e-10) + 1
print(digits)
roof = digits*10
cheap = [roof - item for item in costs]
print(cheap)

max_cheap = knapsack_dp_tabulation(k, eff, cheap, n)
print(f"Maximum value (DP Tabulation): {max_cheap}")
print(roof - max_cheap)