# 시간 1초
# N = 사람 수 ( 1 ~ 1,000 )
# P = 인출 시간 ( 1 ~ 1,000 )

import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

arr.sort()

answer = 0
for i in range(N):
    answer += (N - i) * arr[i]

print(answer)