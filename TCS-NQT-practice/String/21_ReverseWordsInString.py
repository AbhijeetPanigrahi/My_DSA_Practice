def reverse_words_in_string(str):
    str_arr = str.split()
    reverse_str_arr = reversed(str_arr)
    # str_arr.reverse()     --->  In-place reversing
    return " ".join(reverse_str_arr)

def reverse_words_in_string_2(str):
    str_arr = str.split()
    res = []
    for i in range(len(str_arr)-1, -1, -1):
        res.append(str_arr[i])
    return " ".join(res)

def reverse_words_in_string_3(s):
    res = ""
    word = ""

    i = len(s) - 1
    while i >= 0:
        if s[i] != " ":
            word = s[i] + word
        else:
            if word != "":
                if res == "":
                    res = word
                else:
                    res = res + " " + word
                word = ""
        i -= 1

    if word != "":
        if res == "":
            res = word
        else:
            res = res + " " + word

    return res



print(reverse_words_in_string("welcome to the jungle"))
