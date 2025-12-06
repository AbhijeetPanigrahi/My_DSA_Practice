# It's a recursive algo (method that calls itself)
# Efficient for large data sets
# Uses Divide and conquer algo
# TC: (nlogn)

# function to merge subarrays
def merge(arr, low, mid, high):
    left = low
    right = mid+1

    temp = []

    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1
        
    while left <= mid:
        temp.append(arr[left])
        left += 1
    while right <= high:
        temp.append(arr[right])
        right += 1
    

    # copy all the elements of temp to the original arr
    for i in range(low, high+1):
        arr[i] = temp[i-low]


def merge_sort(arr, low, high):
    if low >= high:
        return
    mid = (low+high) // 2
    merge_sort(arr, low, mid)
    merge_sort(arr, mid+1, high)
    merge(arr, low, mid, high)


arr = list(map(int, input().strip("[]").split(",")))

merge_sort(arr, 0, len(arr)-1)

print(arr)

# [6,5,77,2,4,1,58,69,70,68]

