#############   For 1D matrix   ##############

# Case 1: [1,2,3,4,5]
def input_array_format():
    arr = list(map(int, input().strip("[]").split(',')))
    return arr

# Case 2: 1 2 3 4 5
def input_space_separated():
    arr = list(map(int, input().split()))
    return arr

# Case 3: 1,2,3,4,5
def input_comma_separated():
    arr = list(map(int, input().split(',')))
    return arr

# Case with size not given
def input_array_size_not_given():
    arr = []
    while True:
        try:
            num = input().strip()
            if num == "":
                break
            arr.extend(map(int, num.split()))
        except ValueError:
            print("Please enter valid integers separated by space.")
    return arr

def input_array_size_not_given2():
    arr = list(map(int, input().split()))
    return arr



#############   For 2D matrix   ##############


n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
for row in matrix:
    print(row)



# print(input_array_format())
# print(input_space_separated())
# print(input_comma_separated())
# print(input_array_size_not_given2())