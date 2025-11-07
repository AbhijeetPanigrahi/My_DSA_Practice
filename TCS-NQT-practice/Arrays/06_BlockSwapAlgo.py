"""
Input: N = 5, array[] = {1,2,3,4,5} K=2
Output: {3,4,5,1,2}
Explanation: Rotate the array to right by 2 elements.

"""
arr = [1,2,3,4,5]
arr2 = [1,2,3,4,5,6,7]

k = 2
def rotateArrByKelmnts(arr, k):
    n = len(arr)
    arr.reverse()
    arr[n-k:] = reversed(arr[n-k:])
    arr[:n-k]= reversed(arr[:n-k])

rotateArrByKelmnts(arr,k)
print(arr)
rotateArrByKelmnts(arr2,3)
print(arr2)

# arr = [1,2,3,4,5]
# n = len(arr)
# k = 2
# print(arr[n-k:]) # [4, 5]
# print(arr[:n-k]) # [1, 2, 3]

def rotateArrByKelmnts(arr, k):
    n = len(arr)
    k = k % n  # handle cases where k > n

    # Step 1: Reverse the entire array
    arr.reverse()

    # Step 2: Reverse first k elements
    arr[:k] = reversed(arr[:k])

    # Step 3: Reverse remaining n-k elements
    arr[k:] = reversed(arr[k:])
