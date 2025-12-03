# arr = list(map(int,(input().strip("[]").split(","))))

def find_none_repeating_chars(str):
    # find the chars with freq 1
    freq = [0]*26
    res = []

    for ch in str:
        if ch != ' ':
            freq[ord(ch) - ord('a')] += 1
    
    for ch in str:
        if ch != ' ' and freq[ord(ch) - ord('a')] == 1:
            res.append(ch)
    
    return res

print(find_none_repeating_chars("tomato"))
print(find_none_repeating_chars("blockchain technology"))