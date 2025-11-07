def median(arr):
    sorted_arr = sorted(arr)
    n = len(sorted_arr)

    if n%2 != 0:
        median = sorted_arr[n // 2]
    else:
        mid1 = sorted_arr[(n//2) - 1]
        mid2 = sorted_arr[(n//2)]
        median = (mid1 + mid2) / 2
    
    return median

print(median([2,4,1,3,5]))
print(median([2,5,1,7]))
