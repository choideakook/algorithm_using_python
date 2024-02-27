# 시간 1초
# A = 수열 ( 인덱스 : 1 ~ 1,000,000 )
# N = A.len ( 1 ~ 1,000,000 )

import sys

input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
stack, answer= [], [-1] * N

for i in range(N):
    while stack and A[stack[-1]] < A[i]:
        answer[stack.pop()] = A[i]
    stack.append(i)

print(*answer)