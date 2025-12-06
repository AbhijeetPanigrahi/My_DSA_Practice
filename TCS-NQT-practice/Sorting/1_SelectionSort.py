# # Selection sort is not a fast sorting algo, since it uses nested loops to sort
# Useful for small datasets
# TC: O(n^2)

arr = list(map(int, input().strip("[]").split(",")))

def selection_sort(arr):
    for i in range(0, len(arr)-1):
        min_index= i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        
        if min_index != i:
            arr[min_index], arr[i] = arr[i], arr[min_index]

    return arr

print(selection_sort(arr))