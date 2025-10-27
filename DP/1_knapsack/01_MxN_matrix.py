
# Creating a [m x n] matrix 

m = 3 #rows
n = 4 #cols
matrix = [[-1 for _ in range(n)] for _ in range(m)]

value = 1
for i in range(m):
    for j in range(n):
        matrix[i][j] = value
        value += 1

# print(matrix)

W = 3
d = 4

t = [[-1] * (W) for _ in range(d)]

print(t)

