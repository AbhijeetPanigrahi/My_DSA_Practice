arr = [10,5,10,15,10,5, 15]


# Brute force  -    TC: O(n^2), SC: O(n) for visited_arr
def countFreq(arr):
    n = len(arr)
    
    # visited arr
    visited = [False]*n

    for i in range(n):
        if visited[i]:
            continue

        count = 1

        for j in range(i+1, n):
            if arr[j] == arr[i]:
                count += 1
                visited[j] = True
        
        print(arr[i], count)

# countFreq(arr)

# Optimal - Use HashMap/ dictionary  -    TC: O(n), SC: O(n) for dictionary
def countFreq_optimal(arr):
    freq = {}   # empty dictionary
    for i in arr:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    
    for key, value in freq.items():
        print(key, value)

countFreq_optimal(arr)
