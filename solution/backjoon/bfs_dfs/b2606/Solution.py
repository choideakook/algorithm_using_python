# 바이러스
# 1초
# N = computer ( 1 ~ 100 )

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(now):
    count = 1
    visited[now] = True

    for i in range(1, N + 1):
        if nodes[now][i] and not visited[i]:
            count += dfs(i)
    return count

N = int(input())
link = int(input())

visited = [False] * (N + 1)
nodes = [[False] * (N + 1) for _ in range(N + 1)]

for i in range(link):
    x, y = map(int, input().split())
    nodes[x][y] = True
    nodes[y][x] = True

print(dfs(1) - 1)