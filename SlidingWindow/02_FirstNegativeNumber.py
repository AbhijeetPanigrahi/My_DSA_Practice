from collections import deque

def first_negative_in_window(arr, k):
    q = deque()   # will store indices of negative numbers
    result = []

    for i in range(len(arr)):
        # If current element is negative, add its index
        if arr[i] < 0:
            q.append(i)

        # Remove elements out of this window
        while q and q[0] <= i - k:
            q.popleft()

        # Start recording results once the first window is ready
        if i >= k - 1:
            if q:
                result.append(arr[q[0]])   # first negative
            else:
                result.append(0)           # no negative found

    return result


"""

arr = [12, -1, -7, 8, -15, 30, 16, 28], k = 3

i=0 → 12 (not negative) → q=[]
Window not ready

i=1 → -1 (negative) → q=[1]
Window not ready

i=2 → -7 (negative) → q=[1,2]
Window [12,-1,-7] → first neg = arr[1] = -1 → result=[-1]

i=3 → 8 (not negative) → q=[1,2]
Remove out-of-window (i-k=0) → q still [1,2]
Window [-1,-7,8] → first neg = arr[1] = -1 → result=[-1,-1]

i=4 → -15 (negative) → q=[1,2,4]
Remove out-of-window (i-k=1) → q=[2,4]
Window [-7,8,-15] → first neg = arr[2] = -7 → result=[-1,-1,-7]

i=5 → 30 → q=[2,4]
Remove out-of-window (i-k=2) → q=[4]
Window [8,-15,30] → first neg = arr[4] = -15 → result=[-1,-1,-7,-15]

i=6 → 16 → q=[4]
Remove out-of-window (i-k=3) → q=[4]
Window [-15,30,16] → first neg = arr[4] = -15 → result=[-1,-1,-7,-15,-15]

i=7 → 28 → q=[4]
Remove out-of-window (i-k=4) → q=[]
Window [30,16,28] → no negative → result=[-1,-1,-7,-15,-15,0]


"""