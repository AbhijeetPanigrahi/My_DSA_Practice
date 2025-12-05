def sort_characters_in_string(str):
    chars_arr = [ch for ch in str if ch.isalpha()]

    sorted_char_arr = sorted(chars_arr)

    return ''.join(sorted_char_arr)

print(sort_characters_in_string("zxcbg"))

