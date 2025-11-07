def isPalindrome(num):
    revNum = 0

    dup = num

    while num > 0:
        ld = num%10
        revNum =  revNum*10+ld
        num = num // 10
    
    if revNum == dup:
        return True
    return False

print(isPalindrome(4554))
print(isPalindrome(4545))

def isPalindromeInInterval(min, max):
    nums = []
    for i in range(min, max):
        if isPalindrome(i):
            nums.append(i)
    return nums

"""
def isPalindromeInInterval(min, max):
    for i in range(min, max):
        if isPalindrome(i):
            print(i, end=" ")

isPalindromeInInterval(10, 50)

"""