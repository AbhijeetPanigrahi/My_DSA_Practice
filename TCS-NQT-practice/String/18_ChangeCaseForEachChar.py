def change_case_of_each_char_in_string(str):
    result = []
    for ch in str:
        ascii_val = ord(ch)

        if 65 <= ascii_val <= 90:   # if uppercase
            result.append(ch.lower())
        elif 97 <= ascii_val <= 122:   # if lowercase
            result.append(ch.upper())
        else:
            result.append(ch)
    
    return "".join(result)

print(change_case_of_each_char_in_string("abcDe56fG"))