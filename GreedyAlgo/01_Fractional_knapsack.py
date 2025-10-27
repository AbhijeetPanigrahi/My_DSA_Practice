class Item:
    def __init__(self, val, weight):
        self.val = val
        self.weight = weight
    

def fractional_knapsack(items, W):
    items.sort(key= lambda item: item.val/item.weight, reverse=True)
    total_val = 0
    for item in items:
        if item.weight <= W:
            W -= item.weight
            total_val += item.val
        else:
            fraction = W / item.weight
            total_val += item.val * fraction
            break
    return total_val


items = [Item(60, 10), Item(100, 20), Item(120, 30)]
W = 50

print(fractional_knapsack(items, W))