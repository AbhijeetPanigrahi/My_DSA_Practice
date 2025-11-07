def remove_duplicated_inplace(arr):
    n = len(arr)

    i = 0
    for j in range(1, n):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]
    return i+1

nums = [0,0,1,1,1,2,2,3,3,4]
k = remove_duplicated_inplace(nums)
print("Unique count =", k)
print("Array after removing duplicates:", nums[:k])


# We can't do this since:
    # It's taking an extra space also not maintaing the order
"""
def remove_duplicated_unsorted_inplace(arr):
    sorted_arr = sorted(arr)
    n = len(sorted_arr)

    i = 0
    for j in range(1, n):
        if sorted_arr[j] != sorted_arr[i]:
            i += 1
            sorted_arr[i] = sorted_arr[j]
    return i+1

nums = [4,3,9,2,4,1,10,89,34]
k = remove_duplicated_unsorted_inplace(nums)
print("Unique count =", k)
print("Array after removing duplicates:", nums[:k])

"""