total_num_of_coins = [ 1, 2, 5, 10, 20, 50, 100, 500, 1000 ]

def min_num_coins(total_num_of_coins, amount):
    
    ans = []
    for i in range(len(total_num_of_coins)-1, -1, -1):
        while total_num_of_coins[i] <= amount:
                amount -= total_num_of_coins[i]
                ans.append(total_num_of_coins[i])
    return ans

print(min_num_coins(total_num_of_coins, 49))