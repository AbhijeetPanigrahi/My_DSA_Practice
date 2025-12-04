def char_shift(str, len):
    res = []

    for i in range(len):
        ascii_val = ord(str[i])

        if ascii_val == 90: # 90 -> Z
            res.append(chr(65)) # 65 -> A
        elif ascii_val == 122: # 122 -> z
            res.append(chr(97)) # 97 -> a
        elif 65 <= ascii_val <= 90 or 97 <= ascii_val <= 122:
            res.append(chr(ascii_val+1))    # shift one forward
        else:
            res.append(str[i])

    return ''.join(res)

print(char_shift("abcdxyz", len("abcdxyz")))
print(char_shift("abcd xyz", len("abcd xyz")))
