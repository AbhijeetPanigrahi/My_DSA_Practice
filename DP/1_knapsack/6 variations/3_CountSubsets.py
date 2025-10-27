"""
Given an array of integers arr[] and an integer sum, 
find the number of subsets of arr whose sum equals sum.

arr = [2, 3, 5, 6, 8, 10], sum = 10
Output: 3
Explanation: subsets are [10], [2, 8], [5, 3, 2]

"""

def subsetSum(arr, trgt):
    n = len(arr)
    matrix = [[False]*(trgt+1) for _ in range(n+1)]

    # Base case
    for i in range(n+1):
        matrix[i][0] = True
    
    for i in range(1, n+1):
        for j in range(1, trgt+1):
            if arr[i-1] <= trgt:
                matrix[i][j] = matrix[i-1][j-arr[i-1]] + matrix[i-1][j]
            else:
                matrix[i][j] = matrix[i-1][j]
        
    return matrix[n][trgt]

print(subsetSum([3, 34, 4, 12, 5, 2], 9))