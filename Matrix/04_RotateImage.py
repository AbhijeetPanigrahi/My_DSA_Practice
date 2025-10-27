# Brute Force  -  TC = O(n^2), SC = O(n^2) since we are using an extra space which is the ans mat ]

# create an ans matrix and place the elements of the original matrix into the ans matrix with it's correct place
# Observation: first row --> last col, 2nd row --> second last col, ....so on
'''
let's consider a 4x4 matrix
while rotating the change of index:
[0][0] --> [0][3]
[0][1] --> [1][3]
[0][2] --> [2][3]
[0][3] --> [3][3]

[1][0] --> [0][2]
[1][1] --> [1][2]
[1][2] --> [2][2]
[1][3] --> [3][2]

... so on

'''

def rotate_matrix(mat):
    n = len(mat)
    rows = len(mat)
    cols = len(mat[0])

    ans_mat = [[0]*cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            ans_mat[j][n-1-i] = mat[i][j]

    return ans_mat

mat = [
        [5,1,9,11],
        [2,4,8,10],
        [13,3,6,7],
        [15,14,12,16]
      ]

# print(rotate_matrix(mat))


# Better Approach   -  TC = O(n^2), SC = O(1)

# we have to solve it in-place so that the extra space will remove
# Observation: Transpose the matrix (The col becoming the row and the row becoming the col), then just reverse every row

# now how to Transpose?
'''
- all the left digonal elements are same after transpose
- and the elements in the upper and lower are just swapped, like: 

[0][1] = [1][0]
[0][2] = [2][0]
[1][2] = [2][1]
....so on

'''

def rotate_image_optimized(mat):
    for i in range(len(mat)):
        for j in range(i+1, len(mat)):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

    for row in mat:
        row.reverse()

    return mat
     
print(rotate_image_optimized(mat))
