arr = [8,10,5,7,9]

def findSmallest(arr):
    min = float("inf")
    for i in arr:
        if i < min: 
            min = i
    
    return min

print(findSmallest(arr))