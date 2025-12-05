def concatination_of_one_string_to_another(str1, str2):
    res = []
    str1_arr = list(str1)
    str2_arr = list(str2)

    i=0
    while i<len(str1_arr):
        res.append(str1_arr[i])
        i+=1
    
    j = 0
    while j<len(str2_arr):
        res.append(str2_arr[j])
        j+=1
    
    return "".join(res)

print(concatination_of_one_string_to_another("hello", "world"))