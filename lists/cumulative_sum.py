# Given a list of N integers, find the largst sum of K adjacent elements

# inputs
N, K = [int(n) for n in input().split()]
nums = [int(n) for n in input().split()]

# list of cumulative sums
# ith element is the sum of nums[0] + nums[1] + ... + nums[i+1]
cumulative_sums = [0]
for i in range(1, len(nums)+1):
    cumulative_sums.append(cumulative_sums[i-1] + nums[i-1])

k_cumulative_sums = [cumulative_sums[i+K] - cumulative_sums[i] for i in range(N-K+1)]

print(max(k_cumulative_sums))