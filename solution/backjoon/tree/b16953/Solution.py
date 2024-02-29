# A -> B
# 2초
# A = start ( 1 ~ B )
# B = goal ( A ~ 10^9 )

from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    Q = deque()
    Q.append((B, 1))
    while Q:
        now, count = Q.popleft()
        if now == A:
            return count
        if now > A:
            if now % 10 == 1:
                Q.append((int(str(now)[:-1]), count + 1))
            if now % 2 == 0:
                Q.append((now // 2, count + 1))
    return -1

A, B = map(int, input().split())
print(bfs())

