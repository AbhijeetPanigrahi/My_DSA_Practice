def remove_duplicate_chars(str):
    res = []
    seen = [False]*26
    for ch in str:
        if not seen[ord(ch) - ord('a')]:
            seen[ord(ch) - ord('a')] = True
            res.append(ch)
        
    return ''.join(res)

print(remove_duplicate_chars("abhijeet"))