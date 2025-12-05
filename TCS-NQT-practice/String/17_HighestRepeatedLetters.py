def highest_repeated_letter_word_in_string(str):
    # variables for tracking
    curr_max_word = 0
    max_word = 0
    result = ""

    words = str.split()

    # iterate through each word in str
    for word in words:
        freq = [0]*26
        for ch in word:
            freq[ord(ch) - ord('a')] += 1
        
        curr_max_word = 0 # we've to reset here for each word
        for i in freq:
            if i > 1:
                curr_max_word += i
        
        if curr_max_word > max_word:
            max_word = curr_max_word
            result = word
        
    if result == "":
        return -1
    else:
        return result
    

print(highest_repeated_letter_word_in_string("abcdefghij google microsoft"))