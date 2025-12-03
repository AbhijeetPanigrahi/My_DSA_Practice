def maxProductSubArr_optimal(arr):
    n = len(arr)
    pref, suf = 1, 1

    ans = float('-inf')

    for i in range(n):
        if pref == 0:
            pref = 1
        if suf == 0:
            suf = 1
        
        pref *= arr[i]

        suf *= arr[n-i-1]

        ans = max(ans, pref, suf)

    return ans

arr = [2, 3, -2, 4]
print(maxProductSubArr_optimal(arr))