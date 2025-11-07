arr1 = [1,2,4,7,5]
arr2 = [1,2,4,7, 7, 5]
# brute force approach - only valid when there are no duplicates in arr
def findSecondSmallestLargest(arr):     #  TC: O(NlogN), For sorting the array
    n = len(arr)
    if n == 0 or n == 1:
        print(-1, -1)
    arr.sort()
    small = arr[1]
    large = arr[n-2]
    print("Second smallest is", small)
    print("Second largest is", large)

# findSecondSmallestLargest(arr1)



# better approach  -  TC: O(N)
# find the smallest and largest first in one traversal
# then find the second smallest and largest in second traversal
def findSecondSmallestLargest_better(arr):
    n = len(arr)
    if n == 0 or n == 1:
        print(-1, -1)
    
    small = float('inf')
    second_small = float('inf')
    large = float('-inf')
    second_large = float('-inf')
    for i in range(n):
        small = min(small, arr[i])
        large = max(large, arr[i])
    for i in range(n):
        if arr[i] < second_small and arr[i] != small:
            second_small = arr[i]
        if arr[i] > second_large and arr[i] != large:
            second_large = arr[i]
    print("Second smallest is", second_small)
    print("Second largest is", second_large)

# findSecondSmallestLargest_better(arr2)



# best approach  -  TC: O(N)
# do it in one loop
# If the current element is smaller than ‘small’, then we update second_small and small variables
# Else if the current element is smaller than ‘second_small’ then we update the variable ‘second_small’
def findSecondSmallest_best(arr):
    n = len(arr)
    if n == 0 or n == 1:
        print(-1, -1)
    
    small = float('inf')
    second_small = float('inf')
    large = float('-inf')
    second_large = float('-inf')
    for i in arr:
        if i < small:
            small, second_small = i, small
            print(small, second_small)
        elif i < second_small and i != small:
            second_small = i

    print("Second smallest is", second_small)

findSecondSmallest_best(arr2)