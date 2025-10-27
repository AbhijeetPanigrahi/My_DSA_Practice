"""
Pseudo code
----------------------
need = Counter(p)
count = 0
for right in range(n):
    if need[s[right]] > 0: count += 1
    need[s[right]] -= 1
    if count == m: record
    if window full:
        if need[s[left]] >= 0: count -= 1
        need[s[left]] += 1
        left += 1
"""

def find_anagrams_indices(s: str, p: str) -> list:
    """
    Returns list of starting indices of p's anagrams in s.
    Works for lowercase a-z strings. O(n) time, O(1) space.
    """
    n, m = len(s), len(p)
    if m > n or m == 0:
        return []  # nothing to find (you could return 0 if you want the count)

    # need[c] = how many more of char c we still need in the window
    need = [0] * 26
    for ch in p:
        need[ord(ch) - 97] += 1

    left = 0           # left end of sliding window
    count = 0          # how many chars of p are currently matched in the window
    result = []        # record start indices (or increment a counter)

    for right in range(n):
        # include s[right] into the window
        r_idx = ord(s[right]) - 97
        if need[r_idx] > 0:
            # this incoming char was needed -> contributes to matched count
            count += 1
        need[r_idx] -= 1   # we've used one 'r' (could go negative if extra)

        # If we've matched m chars, current window (left..right) is an anagram
        if count == m:
            result.append(left)

        # If window size reached m, move left pointer to keep size constant
        if right - left + 1 == m:
            l_idx = ord(s[left]) - 97
            # If need[l_idx] >= 0 **before** incrementing, then the char at left
            # was contributing to the matched count -> remove that contribution.
            if need[l_idx] >= 0:
                count -= 1
            need[l_idx] += 1  # returning one ch back to the required pool
            left += 1

    return result
