# Brute Force Approach - O(n^2)
arr = [2,5,1,7,10]
k = 14

def longest_subArr(arr, k):
    max_len = 0
    best_sub_arr = []
    n = len(arr)
    for i in range(0, n):
        sum = 0
        for j in range(i, n):
            sum = sum + arr[j]
            if sum <= k: 
                if j-i+1 >= max_len:
                    max_len = max(max_len, j-i+1)
                    best_sub_arr = arr[i : j+1]
            elif sum>k: break
    return max_len
    # return best_sub_arr

print(longest_subArr(arr, k))


# Better Approach - O(n + n) --> O(2n) = O(n)
def longest_substring(s):
    left = 0
    seen = set()
    max_len = 0
    start_index = 0

    for right in range(len(s)):
        # 1. Shrink the window if duplicate found
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        
        # 2. Expand the window
        seen.add(s[right])

        # 2. Update Result
        max_len = max(max_len, right-left+1)
        # if right-left+1 > max_len:
        #     max_len = right-left+1
        #     start_index = left # record starting index of best window
    
    # longest_substring = s[start_index : start_index + max_len]
    return max_len

print(longest_substring("abcabcbb")) # output = abc (3)


# Best/Optimal Approach - Use a Hash Map - O(n)
def longest_substring_optimized(s):
    left = 0
    max_len = 0
    start_index = 0 # only needed if you want to print print the substring (not needed to find the max_len)
    last_index = {} # char -> last seen index

    for right in range(len(s)):
        char = s[right]

        # move/update left i.e shrink the window only when duplicate found without checking all the elements
        if char in last_index and last_index[char] >= left:
            left = last_index[char] + 1  # jump left
        
        last_index[char] = right

        # checking that the current substring is max or not
        if right - left + 1 > max_len:
            max_len = right - left + 1
            start_index = left  # only needed if you want to print print the substring (not needed to find the max_len)

    longest_substring = s[start_index:start_index + max_len]
    print("Longest substring:", longest_substring)
    print("Length:", max_len)
    return longest_substring

longest_substring_optimized("abcabcbb")


"""

right → expanding pointer

left → start of current window

last_index → where we last saw each character

max_len and start_index for best substring

"""