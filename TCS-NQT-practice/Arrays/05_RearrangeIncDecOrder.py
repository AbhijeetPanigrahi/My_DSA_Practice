"""
Input: [8 7 1 6 5 9]
Output: [1 5 6 9 8 7]

"""
arr = [8, 7, 1, 6, 5, 9]
def rearrangeIncDecOrd(arr):
    # Sort the array
    arr.sort()
    n = len(arr)
    # Reverse the second half
    arr[n//2:] = reversed(arr[n//2:])

rearrangeIncDecOrd(arr)
print(arr)

# n = len(arr)
# arr.sort()
# print(arr[n//2:])
# rev = list(reversed(arr[n//2:]))
# print(rev)