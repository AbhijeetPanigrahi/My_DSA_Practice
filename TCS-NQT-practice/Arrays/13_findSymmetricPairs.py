def findSymmetricPairs(arr):
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i][1] == arr[j][0] and arr[i][0] == arr[j][1]:
                print(f"({arr[i][1], arr[i][0]})")


arr = [(1, 2), (2, 1), (3, 4), (4, 5), (5, 4)]  # Example input
findSymmetricPairs(arr)