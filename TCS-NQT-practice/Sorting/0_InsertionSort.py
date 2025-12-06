# Insertion Sort is not a fast sorting algo, since it uses nested loops to sort
# Useful for small datasets
# TC: O(n^2)

arr = list(map(int, input().strip("[]").split(",")))

def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i-1, -1, -1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            else:
                break
    
    return arr

def insertion_sort_2(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]        # current element to insert
        j = i - 1

        # shift elements greater than key to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # place key at its correct position
        arr[j + 1] = key

    return arr


print(insertion_sort(arr))