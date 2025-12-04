def print_duplicate_chars(str):
    freq = [0]*26
    str = str.lower()
    for ch in str:
        freq[ord(ch) - ord('a')] += 1
    
    for i in range(26):
        if freq[i] > 1:
            print(f"{chr(i + ord('a'))} : {freq[i]}")

print_duplicate_chars("Abhijeet")