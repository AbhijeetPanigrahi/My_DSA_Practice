# Brute force - O(mxn), O(1)
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3

def searchInMatrix(matrix, target):
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == target:
                return True
    
    return False

# print(searchInMatrix(matrix, target))


# Better Approach - O(n) + log(m), O(1)

# As you can see the arr is sorted 
    # so if we just check the first and the last element in every row
    # and check if the target is present or not, we can search the trgt more efficiently
    # And if there is a row we find where the target element can be present then we can apply binary search in that Single row which is 1D matrix/arr

def binary_search(arr,trgt):
    left, right = 0, len(arr)-1
    while(left <= right):
        mid = left + (right-left) // 2
        if trgt == arr[mid]: return mid
        if trgt < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1

def searchInMatrix_better(matrix, target):
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        if matrix[i][0] <= target and matrix[i][cols-1] >= target:
            result = binary_search(matrix[i], target)
            if result != -1:
                return True
    return False
# print(searchInMatrix_better(matrix, target))


# Best/Optimized Approach - O(log(n*m))

# flatten the matrix into a 1D arr -- it's a hypothetical arr you're thinking, not actually have to 
def searchInMatrix_optimized(matrix, target):
    rows = len(matrix)
    cols = len(matrix[0])
    low, high = 0, (rows*cols)-1    # this is like left, right in bs

    while low <= high:
        mid = low + (high-low) // 2
        r, c = mid // cols, mid % cols  # Map the 1D 'mid' index back to 2D indices (r, c)
        if target == matrix[r][c]: return True
        if target < matrix[r][c]: 
            high = mid-1
        else: 
            low = mid+1
    return False

print(searchInMatrix_optimized(matrix, target))
