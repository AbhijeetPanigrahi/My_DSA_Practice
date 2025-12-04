def remove_char_from_firstString_present_in_secondString(str1, str2):
    # str1 = list(str1)
    removed_set = set(str2)

    res = []

    for ch in str1:
        if ch not in removed_set:
            res.append(ch)
    
    return ''.join(res)

print(remove_char_from_firstString_present_in_secondString("abcdef", "cefz"))