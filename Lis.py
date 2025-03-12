def longest_increasing_subsequence(arr):
    if not arr:
        return 0
    dp = [1] * len(arr)
    for i in range(len(arr)):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

# Example usage
print(longest_increasing_subsequence([10, 22, 9, 33, 21, 50, 41, 60, 80]))
