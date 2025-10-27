# Brute force - O(mxn), O(1)
matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5

def searchInMatrix(matrix, target):
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == target:
                return True
    
    return False

# print(searchInMatrix(matrix, target))


# Best/Optimized Approach - O(n+m)

def searchInMatrix_optimized(matrix, target):
    rows = len(matrix)
    cols = len(matrix[0])
    # Start the search from the top-right corner
    r = 0
    c = cols-1
    
    while r < rows and c >= 0:
        if target == matrix[r][c]:
            return True
        if target < matrix[r][c]:
            c -= 1
        else:
            r += 1
    return False
print(searchInMatrix_optimized(matrix, target))
