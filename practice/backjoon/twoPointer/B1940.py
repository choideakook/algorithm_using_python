# 주몽
# N = length
# M = target ( 1 ~ 10^7 )
# num = 재료 ( 1 ~ 15,000 )

import sys

def twoSum(nums, M, N):
    nums.sort()
    l, r = 0, N - 1

    count = 0
    while l < r:
        sum = nums[l] + nums[r]

        if sum < M:
            l += 1
        elif sum > M:
            r -= 1
        else:
            count += 1
            l += 1
            r -= 1
    return count

input = sys.stdin.readline

N = int(input())
M = int(input())
nums = list(map(int, input().split()))
print(twoSum(nums, M, N))