def checkPalindrome(i, s):
    # base condition: if the i covers half of the string then we must know the ans
    if i >= len(s) // 2:
        return True
    
    # check first and last element (if equal then palindrome otherwise not)
    if s[i] != s[len(s)-i-1]:
        return False
    
    # then recursively do start+1 and end-1
    return checkPalindrome(i+1, s)


s = "madam"
s1 = "abhi"
print(checkPalindrome(0, s1))