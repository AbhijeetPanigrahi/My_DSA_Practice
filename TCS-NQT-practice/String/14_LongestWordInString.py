def longest_word_in_string(str):
    n = len(str)
    i, j = 0, 0
    max_length = 0
    max_start = 0

    while j <= n:
        if j < n and str[j] != ' ':
            j += 1
        else:
            curr_len = j - i

            if curr_len > max_length:
                max_length = curr_len
                max_start = i
            
            j += 1
            i = j
        
    return str[max_start : max_start+max_length]


print(longest_word_in_string("Google Doc"))