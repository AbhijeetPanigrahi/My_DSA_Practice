arr = list(map(int, input().strip("[]").split(",")))

def findRepeating_1(arr):
    freq = {}
    result = []

    # Step 1: Count frequencies
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    # Step 2: Collect repeating elements only once
    for num, count in freq.items():
        if count > 1:
            result.append(num)
            
    return result

print(findRepeating_1(arr))


#############  OR  ###############

def findRepeating(arr):
    freq = {}
    result = []
    
    for num in arr:
        if num in freq:
            if num not in result:
                result.append(num)
        else:
            freq[num] = 1

    return result

# [10,5,10,15,10,5, 15]
# [1,1,2,3,4,4,5,2]
