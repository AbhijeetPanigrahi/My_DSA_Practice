# n = int(input())
# arr = list(map(int, input().split()))

# for num in arr:
#     print(num, end=" ")



input_str = input()
#Split the input string based on spaces
numbers = input_str.split()
arr = [int(num) for num in numbers]
#Print the numbers with a space in between
print(" ".join(map(str, arr)))



input_str = input()
#Split the input string based on commas
numbers = input_str.split(",")
arr = [int(num) for num in numbers]
# Print the numbers with a space in between
print(" ".join(map(str, arr)))