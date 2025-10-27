from collections import Counter

def find_anagrams_indices_shorter(s: str, p: str) -> list:
    n, m = len(s), len(p)
    if m > n:
        return []

    # Use Counter for character frequency maps
    p_map = Counter(p)
    window_map = Counter(s[:m - 1])
    result = []

    for i in range(m - 1, n):
        # Add a new character to the window
        window_map[s[i]] += 1
        
        # Check if the current window is an anagram
        if window_map == p_map:
            result.append(i - m + 1)
        
        # Remove the character leaving the window
        window_map[s[i - m + 1]] -= 1
        if window_map[s[i - m + 1]] == 0:
            del window_map[s[i - m + 1]]
            
    return result

s = "cbaebabacd"
p = "abc"

print(find_anagrams_indices_shorter(s,p))