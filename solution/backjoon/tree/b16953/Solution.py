# A -> B
# 2초
# A = start ( 1 ~ B )
# B = goal ( A ~ 10^9 )

import sys
input = sys.stdin.readline

def dfs():
    Q = []
    Q.append(A)
    while Q:
        now = Q.pop(0)
        square = now * 2
        add = (now * 10) + 1
        if square == B or add == B:
            return visited[B] + visited[now]
        if square < B:
            if visited[square] == 1:
                visited[square] += visited[now]
                Q.append(square)
        if add < B:
            if visited[add] == 1:
                visited[add] += visited[now]
                Q.append(add)
    return -1

A, B = map(int, input().split())
visited = [1] * (B + 1)
print(dfs())

