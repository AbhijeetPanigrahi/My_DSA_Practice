wt = [1, 3, 4, 5]   # weight
val = [1, 4, 5, 7]
W = 7
n = len(wt)

matrix = [[-1] * (W+1) for _ in range(n+1)]

def knapsack_memoization(wt, val, W, n, matrix):
    if W == 0 or n == 0:    # base condition
        return 0
    
    if matrix[n][W] != -1:
        return matrix[n][W]
    
    if wt[n-1] <= W:
        matrix[n][W] = max(val[n-1]+knapsack_memoization(wt, val, W-wt[n-1], n-1, matrix),
                   knapsack_memoization(wt, val, W, n-1, matrix))
    elif wt[n-1] > W:
        matrix[n][W] = knapsack_memoization(wt, val, W, n-1, matrix)
    
    return matrix[n][W]


print(knapsack_memoization(wt, val, W, n, matrix))



# Using memo:

"""
from typing import List

def knapsack(weights: List[int], values: List[int], capacity: int) -> int:
    n = len(weights)
    memo = {}

    def dfs(i, w):
        # Base case: no items left or no capacity left
        if i == n or w == 0:
            return 0

        if (i, w) in memo:
            return memo[(i, w)]

        # Option 1: skip the current item
        not_take = dfs(i + 1, w)

        # Option 2: take the current item (if it fits)
        take = 0
        if weights[i] <= w:
            take = values[i] + dfs(i + 1, w - weights[i])

        # Store result in memo
        memo[(i, w)] = max(take, not_take)
        return memo[(i, w)]

    return dfs(0, capacity)

"""