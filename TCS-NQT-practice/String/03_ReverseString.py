# reversal done in-place (so O(1) Space Complexity)
def reverseString(str):
    str = list(str)

    left = 0
    right = len(str)-1

    while left < right:
        str[left], str[right] = str[right], str[left]

        left += 1
        right -= 1

    return ''.join(str)

print(reverseString("hello"))
print(reverseString("I am iron man"))