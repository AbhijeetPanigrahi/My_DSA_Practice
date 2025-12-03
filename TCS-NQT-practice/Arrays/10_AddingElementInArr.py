def insertAtBegining(arr, num):
    # result = [0]*(len(arr)+1)
    # result[0] = num
    # for i in range(1, len(result)):
    #     result[i] = arr[i-1]

    # return result
    arr.append(0)
    n = len(arr)
    for i in range(n-2, -1, -1):
        arr[i+1] = arr[i]
    arr[0] = num

arr = [1,2,3,4,5]
# print(insertAtBegining(arr,7))
insertAtBegining(arr, 7)
print(arr)
insertAtBegining(arr,12)
print(arr)






def insertAtPos(arr, index, value):
    
    n = len(arr)
    
    # mimic Python list.insert behavior: clamp index
    if index <= 0:
        index = 0
    elif index > n:
        index = n

    # make space for one more element
    arr.append(None)

    # shift elements right starting from last real element down to index
    # i goes: n-1, n-2, ..., index
    for i in range(n - 1, index - 1, -1):
        arr[i + 1] = arr[i]
    
    # place the new value
    arr[index] = value



a = [1, 2, 3, 4, 5]
insertAtPos(a, 2, 99)
print(a)           # [1, 2, 99, 3, 4, 5]

b = [1, 2, 3]
insertAtPos(b, 0, 7)
print(b)           # [7, 1, 2, 3]

c = [1, 2, 3]
insertAtPos(c, 10, 9)
print(c)           # [1, 2, 3, 9]  (index >= len -> append)

d = []
insertAtPos(d, 0, 42)
print(d)  