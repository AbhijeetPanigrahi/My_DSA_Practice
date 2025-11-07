def isPrime(n):
    cnt = 0
    for i in range(1, n+1):
        if n % i == 0:
            cnt += 1
    
    if cnt == 2:
        return True

    return False

# ##########################################

import math

def isPrime_optimized(n):
    cnt = 0
    for i in range(1, int(math.sqrt(n))+1):     # without 'math' -> int(n**0.5)
        if n % i == 0:
            cnt += 1

            if n // i != i:
                cnt += 1
    
    if cnt == 2:
        return True

    return False

print(isPrime(4))
print(isPrime_optimized(5))