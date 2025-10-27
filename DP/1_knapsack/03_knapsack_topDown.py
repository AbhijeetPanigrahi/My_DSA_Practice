wt = [1, 3, 4, 5]   # weight
val = [1, 4, 5, 7]
W = 7
n = len(wt)

matrix = [[0]*(W+1) for _ in range(n+1)]
"""
for i in range(n+1):
    dp[i][0] = 0
for j in range(W+1):
    dp[0][j] = 0
"""

def knapsack_topDown(wt, val, W, n):
    for i in range(1, n+1):
        for j in range(1, W+1):
            if wt[i-1] <= j:
                matrix[i][j] = max(val[i-1] + matrix[i-1][j-wt[i-1]] , matrix[i-1][j])
            else:
                matrix[i][j] = matrix[i-1][j]

    return matrix[n][W]

print(knapsack_topDown(wt, val, W, n))
