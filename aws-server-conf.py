def reversed_knapsack(eff, costs, target_eff):
    n = len(eff)
    max_eff = sum(eff)
    INF = float('inf')

    # dp[v] = min weight to reach value v
    dp = [INF] * (max_eff + 1)
    dp[0] = 0

    for i in range(n):
        for v in range(max_eff, eff[i] - 1, -1):
            if dp[v - eff[i]] != INF:
                dp[v] = min(dp[v], dp[v - eff[i]] + costs[i])

    # Find the minimum weight for value >= target_value
    result = min(dp[v] for v in range(target_eff, max_eff + 1))
    return result if result != INF else -1  # -1 if it's not possible

# Example usage
eff = [4, 4, 6, 7]
costs = [1, 1, 2, 2]
k = 7

eff = [75, 104, 72,72,8,125]
costs = [1, 2, 2, 1, 2, 1]
k = 376

min_cost = reversed_knapsack(eff, costs, k)
print(f"Minimum weight to achieve at least {k} value: {min_cost}")
