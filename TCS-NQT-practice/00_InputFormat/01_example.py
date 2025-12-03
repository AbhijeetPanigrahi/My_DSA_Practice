
a, b = map(int, input().split())
print(a + b)

"""
input(): This function prompts the user for input and reads an entire line of text as a string.
For example, if the user types "10 20" and presses Enter, input() returns the string "10 20".

.split(): This is a string method that splits a string into a list of substrings based on a delimiter. 
When called without any arguments, it splits the string by whitespace characters (spaces, tabs, newlines). 
Continuing the example, "10 20".split() would result in the list ["10", "20"]

map(int, ...): The map() function applies a given function to each item in an iterable. 
In this case, int is the function, and the list ["10", "20"] is the iterable.
"""


t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(a + b)


import sys
for line in sys.stdin:
    a, b = map(int, line.split())
    print(a + b)


import sys
data = sys.stdin.read().strip().split()
