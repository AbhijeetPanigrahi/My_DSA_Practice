"""
Given an array of integers arr[] and a value sum, determine 
if there is a subset of the array whose sum equals sum.

arr = [3, 34, 4, 12, 5, 2]
sum = 9
Output: True   (because 4 + 5 = 9)

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
                matrix[i][j] = matrix[i-1][j-arr[i-1]] or matrix[i-1][j]
            else:
                matrix[i][j] = matrix[i-1][j]
        
    return matrix[n][trgt]

print(subsetSum([3, 34, 4, 12, 5, 2], 9))