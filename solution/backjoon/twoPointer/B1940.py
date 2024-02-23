# 주몽
# N = length
# M = target ( 1 ~ 10^7 )
# num = 재료 ( 1 ~ 15,000 )

import sys

def twoSum(nums, target):
    map = {}
    answer = 0
    for num in nums:
        if target - num in map: answer += 1
        else: map[num] = nums
    return answer

input = sys.stdin.readline

N = int(input())
M = int(input())
nums = list(map(int, input().split()))
print(twoSum(nums, M))