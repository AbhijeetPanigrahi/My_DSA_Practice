def replaceElementByRank(arr):
    sorted_arr = sorted(arr)

    rank_map = {}

    rank = 1

    for num in sorted_arr:
        if num not in rank_map:
            rank_map[num] = rank
            rank += 1

    result = [rank_map[num] for num in arr]
    return result

print(replaceElementByRank([20, 15, 26, 2, 98, 6]))