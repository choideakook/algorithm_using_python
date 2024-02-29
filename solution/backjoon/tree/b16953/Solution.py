# A -> B
# 2초
# A = start ( 1 ~ B )
# B = goal ( A ~ 10^9 )

import sys
input = sys.stdin.readline

def dfs():
    Q = []
    Q.append(B)
    while Q:
        now = Q.pop(0)
        if now == A: return visited[A]
        if now % 10 == 1:
            num = int(str(now)[:-1])
            visited[num] += visited[now]
            Q.append(num)
        if now % 2 == 0:
            if now // 2 >= A:
                visited[now // 2] += visited[now]
                Q.append(now // 2)
    return -1

A, B = map(int, input().split())
visited = [1] * (B + 1)
print(dfs())

