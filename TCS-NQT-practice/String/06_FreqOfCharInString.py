def freq_of_chars_in_string(str):
    freq = [0]*26
    for ch in str:
        freq[ord(ch) - ord('a')] += 1
    
    for i in range(26):
        if freq[i] != 0:
            print(f"{chr(i+ord('a'))}{freq[i]}", end=" ")
    
freq_of_chars_in_string("takeuforward")