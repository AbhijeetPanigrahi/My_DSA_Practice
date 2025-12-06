# Selecting the pivot is the key to the success of Quick Sort
# It's also a Recursive Algo
# TC: O(NlogN)

arr = list(map(int, input().strip("[]").split(",")))

def quick_sort(arr):
    # base case (since it's a recursive algo)
    if len(arr) <= 1:
        return arr
    
    # pivot element (let's take last element)
    p = arr[-1]

    L = [x for x in arr[:-1] if x <= p]
    R = [x for x in arr[:-1] if x > p]

    L = quick_sort(L)
    R = quick_sort(R)

    return L + [p] + R

print(quick_sort(arr))

