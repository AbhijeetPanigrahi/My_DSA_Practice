def subarray_sum_divisible(arr, k):
    prefix = 0              # keeps running prefix sum
    seen = set()            # stores remainders we have seen so far
    
    for num in arr:
        prefix += num       # update running prefix sum
        
        # Compute remainder when divided by k
        remainder = prefix % k
        
        # Two important cases:
        # Case 1: If remainder == 0 → it means prefix sum itself is divisible by k
        #   Example: arr=[2,3], k=5 → prefix=5, remainder=0 → subarray [2,3]
        #
        # Case 2: If remainder is already in 'seen':
        #   It means we found two prefix sums with same remainder.
        #   Subarray between them must be divisible by k.
        #   Why? (prefix[j] - prefix[i]) % k = 0 → divisible by k.
        #
        if remainder == 0 or remainder in seen:
            return True     # found a valid subarray
        
        # Otherwise, record this remainder for future checks
        seen.add(remainder)
    
    # If no valid subarray found
    return False


"""

if two prefix sums have the same remainder when divided by k,
the sum of subarray between them is divisible by k.


Example Dry Run
---------------------------

arr = [1, 2, 3], k = 5

Start: prefix=0, seen={}

num=1 → prefix=1, remainder=1
→ not 0, not in seen → add remainder → seen={1}

num=2 → prefix=3, remainder=3
→ not 0, not in seen → add remainder → seen={1,3}

num=3 → prefix=6, remainder=1
→ remainder=1 already in seen ✅ → return True
(subarray [2,3] has sum=5 divisible by 5)

"""
