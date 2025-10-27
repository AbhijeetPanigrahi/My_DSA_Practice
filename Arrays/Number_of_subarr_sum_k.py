# Brute Force - O(n^3)
def number_of_subarr_sum_k_brute(arr,k):
    count = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            sum = 0
            for s in range(i,j+1):
                sum = sum + arr[s]

            if sum == k:
                count += 1
    
    return count

arr = [1,2,3,-3,1,1,1,4,2,-3]
print(number_of_subarr_sum_k_brute(arr, 3))


# Better Solution - O(n^2)
def number_of_subarr_sum_k_better(arr,k):
    count = 0
    for i in range(len(arr)):
        sum = 0
        for j in range(i, len(arr)):
            sum += arr[j]
            if sum == k:
                count += 1
    
    return count

print(number_of_subarr_sum_k_better(arr, 3))


# Optimal Solution -  O(n)
def number_of_subarr_sum_k_optimal(arr, k):
    # We record that prefix sum 0 has been seen once: this accounts for subarrays that start at index 0.
    prefix_count = {0: 1}
    current_sum = 0     # it is the running prefix sum P(j)
    count = 0  # accumulates the number of subarrays found.

    for num in arr:
        current_sum += num  # Update prefix sum to P(j)
        # Check how many previous prefix sums equal P(j) - k. Each occurrence corresponds to a subarray that ends at j and sums to k.
        if (current_sum - k) in prefix_count:
            # Add that many subarrays to the result.
            count += prefix_count[current_sum - k]
        # Record that this prefix sum has now been seen once more (so future j can match against it) 
        prefix_count[current_sum] = prefix_count.get(current_sum, 0) + 1

    return count