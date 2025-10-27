def build_prefix_sum(matrix):
    n, m = len(matrix), len(matrix[0])
    pre = [[0] * m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            pre[i][j] = matrix[i][j]
            
            if i > 0: pre[i][j] += pre[i-1][j]      # add top
            if j > 0: pre[i][j] += pre[i][j-1]      # add left
            if i > 0 and j > 0: pre[i][j] -= pre[i-1][j-1]  # subtract overlap
    
    return pre


def submatrix_sum(pre, r1, c1, r2, c2):
    res = pre[r2][c2]
    if r1 > 0: res -= pre[r1-1][c2]
    if c1 > 0: res -= pre[r2][c1-1]
    if r1 > 0 and c1 > 0: res += pre[r1-1][c1-1]
    return res


# Example
mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

pre = build_prefix_sum(mat)
print(submatrix_sum(pre, 1, 1, 2, 2))  # sum of [[5,6],[8,9]] = 28
print(submatrix_sum(pre, 0, 0, 1, 1))  # sum of [[1,2],[4,5]] = 12
