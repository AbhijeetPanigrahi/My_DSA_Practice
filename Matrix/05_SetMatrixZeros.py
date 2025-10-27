# Brute force   -  TC: O((m*n)*(m+n)+(m*n)) ---> O(n^3)
def set_matrix_zeros(mat):
    rows = len(mat)
    cols = len(mat[0])

    def row_mark(i):
        for j in range(rows):
            if mat[i][j] != 0:
                mat[i][j] = -1

    def col_mark(j):
        for i in range(cols):
            if mat[i][j] != 0:
                mat[i][j] = -1


    for i in range(rows):
        for j in range(cols):
            if mat[i][j] == 0:
                row_mark(i)
                col_mark(j)

    for i in range(rows):
        for j in range(cols):
            if mat[i][j] == -1:
                mat[i][j] = 0

    return mat

matrix = [[1,1,1],[1,0,1],[1,1,1]]
print(set_matrix_zeros(matrix))



# Better Solution   -  TC: O(2*n*m), SC: O(n) + O(m) --> for the 2 arrs we're using for hashing

def set_matrix_zeros_better(mat):
    rows = len(mat)
    cols = len(mat[0])

    # 2 imaginary arrays for tracking
    img_row = [0]*rows
    img_col = [0]*cols

    for i in range(rows):
        for j in range(cols):
            if mat[i][j] == 0:
                img_col[i], img_row[j] = 1, 1   # mark it 1 for tracking

    for i in range(rows):
        for j in range(cols):
            if (img_row[i] == 0 or img_col[j] == 0):
                mat[i][j] = 0

    return mat

print(set_matrix_zeros_better(matrix))


# Best/Optimized Approach

# We know to traverse the whole matrix The minimum time complexity is O(n^2), We can't do better than that
# lets just focus on space complexity and optimise it

# Instead of taking two imaginary arrays outside, we can consider inside the matrix, like:
# col[0] --> row[n] and row[0] --> col[m]

