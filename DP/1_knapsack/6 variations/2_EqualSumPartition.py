"""
Given an array of integers, 
determine if it can be partitioned into two subsets such that the total of both subsets is the same.

arr = [1, 5, 11, 5]
Output: True
Explanation: [1, 5, 5] and [11] → both have total = 11

"""

def EqualSumPartition(arr):

    total = sum(arr)

    if total % 2 != 0:
        return False
    
    trgt = total // 2
    n = len(arr)
    matrix = [[False]*(trgt+1) for _ in range(n+1)]

    # Base case
    for i in range(n+1):
        matrix[i][0] = True
    
    for i in range(1, n+1):
        for j in range(1, trgt+1):
            if arr[i-1] <= trgt:
                matrix[i][j] = matrix[i-1][j-arr[i-1]] or matrix[i-1][j]
            else:
                matrix[i][j] = matrix[i-1][j]
        
    return matrix[n][trgt]

print(EqualSumPartition([1, 5, 11, 5]))