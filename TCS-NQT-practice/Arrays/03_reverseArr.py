arr = [1,2,3,4,5]

print(arr[::-1])

# Recursive - O(N), O(1)
def reverseArrRecursive(arr, start, end):
    if start < end:
        arr[start], arr[end] =  arr[end], arr[start]
        reverseArrRecursive(arr, start+1, end-1)
    
reverseArrRecursive(arr, 0, len(arr)-1)
print(arr)


# iterative
def reverseArray(arr, n):
    p1 = 0
    p2 = n - 1
    while p1 < p2:
        arr[p1], arr[p2] = arr[p2], arr[p1]
        p1 += 1
        p2 -= 1

reverseArray(arr, len(arr))
print(arr)