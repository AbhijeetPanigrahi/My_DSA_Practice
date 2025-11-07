def remove_duplicate_unsorted_list(arr):
    n = len(arr)
    seen = {}
    answer_arr = []

    for i in arr:
        if i not in seen:
            answer_arr.append(i)
            seen[i] = True
    
    return answer_arr

nums = [4,3,9,2,4,1,10,89,34]
print(remove_duplicate_unsorted_list(nums))
