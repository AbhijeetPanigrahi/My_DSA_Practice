def build_prefix_2d(mat):
    n, m = len(mat), len(mat[0])
    pre = [[0]*(m+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(m):
            pre[i+1][j+1] = mat[i][j] + pre[i][j+1] + pre[i+1][j] - pre[i][j]
    return pre

def submatrix_sum(pre, r1, c1, r2, c2):
    # using padded pre: indexes shifted by +1
    return pre[r2+1][c2+1] - pre[r1][c2+1] - pre[r2+1][c1] + pre[r1][c1]


mat = [
 [1,2,3],
 [4,5,6],
 [7,8,9]
]

pre = build_prefix_2d(mat)
print(submatrix_sum(pre, 1, 1, 2, 2))   # 28