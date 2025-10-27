# Creating Prefix Sum Array
arr = [2, 4, 6, 8]
n = len(arr)
pre = [0] * n
pre[0] = arr[0]

for i in range(1, n):
    pre[i] = pre[i-1] + arr[i]

# Range Sum Queries
def range_sum(pre, L, R):
    if L == 0:
        return pre[R]
    return pre[R] - pre[L-1]


"""

Derive range sum:
pre[R] = arr[0] + ... + arr[L-1] + arr[L] + ... + arr[R]
pre[L-1] = arr[0] + ... + arr[L-1]

So pre[R] - pre[L-1] = arr[L] + ... + arr[R]

"""