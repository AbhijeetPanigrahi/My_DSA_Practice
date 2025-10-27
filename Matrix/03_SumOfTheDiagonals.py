# 2 types of Sqaure matrix : even length & odd length
# In even length square matrix -> there is no overlapping element
# In odd length square matrix -> there is a overlapping element which is the middle elmnt

# Pseudo code:
"""
- Find the sum of the left diagonal
- Find the sum of the right diagonal
- add these two sums
- Check the length of the matrix, if it's even you've the ans and if it's odd then just subtract the middle element
"""

def diagonal_sum(matrix):
    rows = len(matrix)
    sum = 0
    n = len(matrix)
    for i in range(rows):
        sum += matrix[i][i]
        sum += matrix[i][len(matrix)-i-1]
    
    if rows % 2 != 0:
        sum -= matrix[len(matrix)//2][len(matrix)//2]
    
    return sum

mat_1 = [[1,2,3],
       [4,5,6],
       [7,8,9]]
mat_2 =[[1,1,1,1],
        [1,1,1,1],
        [1,1,1,1],
        [1,1,1,1]]
mat_3 = [[5]]
print(diagonal_sum(mat_3))