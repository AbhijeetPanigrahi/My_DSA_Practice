arr = list(map(int, input().strip("[]").split(",")))

def findNonRepeating(arr):
    freq = {}
    result = []

    # Step 1: Count frequencies
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    # Step 2: Collect elements that appear only once
    for num in arr:
        if freq[num] == 1:
            result.append(num)

    return result

print(findNonRepeating(arr))
