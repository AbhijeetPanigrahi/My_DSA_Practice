# TC: O(n^2)


arr = list(map(int, input().strip("[]").split(",")))

def bubble_sort(arr):
    for i in range(0, len(arr)-1):
        for j in range(0, len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

print(bubble_sort(arr))