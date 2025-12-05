def position_of_substring_within_string(text, pattern):
    N = len(text)
    M = len(pattern)

    for i in range(0, N-M+1):
        temp = i    # since we need the first index
        
        for j in range(0, M):
            if text[temp] != pattern[j]:
                break

            temp += 1

        if j == M-1 and text[temp-1] == pattern[M-1]:
            return i

    return -1


print(position_of_substring_within_string("takeuforward","forward"))



# OPTIMAL
"""
def found_index(text: str, pattern: str) -> int:
    # delegate to str.find (returns -1 if not found)
    return text.find(pattern)
"""