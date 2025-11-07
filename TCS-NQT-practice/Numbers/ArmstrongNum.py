def isArmstrong(n):
    k = len(str(n))

    num = n

    sum = 0

    while num>0:
        ld = num%10
        sum += ld ** k
        num = num//10
    
    return sum == n

print(isArmstrong(371))