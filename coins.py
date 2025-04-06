import math

def min_coin_change(coins, amount):
  """
  Calculates the minimum number of coins needed to make a target amount.

  Args:
    coins: A list of integers representing coin denominations.
    amount: An integer representing the target amount.

  Returns:
    An integer representing the minimum number of coins, or -1 if the
    amount cannot be made.
  """
  # dp[i] will store the minimum number of coins needed to make amount i.
  # Initialize with a value larger than any possible answer (amount + 1 or infinity).
  # Using math.inf for clarity, but amount + 1 also works as max coins needed is amount (if coin 1 exists)
  dp = [math.inf] * (amount + 1)

  # Base case: 0 coins are needed to make amount 0.
  dp[0] = 0

  # Iterate through all amounts from 1 up to the target amount.
  for a in range(1, amount + 1):
    # For each amount, try using each available coin denomination.
    for coin in coins:
      # If the coin value is less than or equal to the current amount 'a'
      if coin <= a:
        # Check if the remaining amount (a - coin) is reachable
        if dp[a - coin] != math.inf:
           # Update dp[a] if using this 'coin' results in fewer total coins
           # than the current minimum stored in dp[a].
           # (1 for the current coin + minimum coins for the remainder)
           dp[a] = min(dp[a], 1 + dp[a - coin])

  for a in range(1, amount + 1):
    print(f"{a}==>{dp[a]}")
  # After filling the table, dp[amount] holds the minimum coins for the target amount.
  # If it's still infinity, the amount is not reachable.
  return dp[amount] if dp[amount] != math.inf else -1

# --- Example Usage ---

coin_denominations1 = [1, 2, 5]
target_amount1 = 2
min_coins = min_coin_change(coin_denominations1, target_amount1)
print(f"Coins: {coin_denominations1}, Amount: {target_amount1}")
print(f"Minimum coins needed: {min_coins}") # Output: 3 (5 + 5 + 1)


coin_denominations1 = [1, 2, 5]
target_amount1 = 11
min_coins = min_coin_change(coin_denominations1, target_amount1)
print(f"Coins: {coin_denominations1}, Amount: {target_amount1}")
print(f"Minimum coins needed: {min_coins}") # Output: 3 (5 + 5 + 1)

coin_denominations2 = [2, 5]
target_amount2 = 3
min_coins2 = min_coin_change(coin_denominations2, target_amount2)
print(f"\nCoins: {coin_denominations2}, Amount: {target_amount2}")
print(f"Minimum coins needed: {min_coins2}") # Output: -1 (Cannot make 3 with only 2s and 5s)

coin_denominations3 = [9, 6, 5, 1]
target_amount3 = 11
min_coins3 = min_coin_change(coin_denominations3, target_amount3)
print(f"\nCoins: {coin_denominations3}, Amount: {target_amount3}")
print(f"Minimum coins needed: {min_coins3}") # Output: 2 (6 + 5)