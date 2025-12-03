def max_occuring_char_in_string(str):
    
    arr = sorted(str)
    
    max_freq, curr_freq = 1, 1
    max_char = arr[0]

    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]:
            curr_freq += 1
        else:
            if curr_freq > max_freq:
                max_freq = curr_freq
                max_char = arr[i-1]
            curr_freq = 1
    
    if curr_freq > max_freq:
        max_freq = curr_freq
        max_char = arr[-i]
    
    return max_char


print(max_occuring_char_in_string("takeuforward"))