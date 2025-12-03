def check_anagrams(str1, str2):
    if len(str1) != len(str2):
        return False
    
    n = len(str1)
    
    freq = [0]*26
    
    for ch in str1:
        freq[ord(ch) - ord('a')] += 1
    
    for ch in str2:
        freq[ord(ch) - ord('a')] -= 1

    for i in freq:
        if i != 0:
            return False
    
    return True


print(check_anagrams("listen", "silent"))  # True
print(check_anagrams("hello", "world"))   # False
    

    