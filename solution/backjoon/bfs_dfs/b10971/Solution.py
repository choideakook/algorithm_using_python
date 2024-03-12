# 외판원 순회 2
# 2초

# N = cities ( 2 ~ 10 )
# W[i][j] = moving cost from i to j  ( 0 ~ 1,000,000 )

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(now):
    to, price = -1, 1000001
    for i in range(N):
        if 0 < node[now][i] < price and not visited[i]:
            to, price = i, node[now][i]

    if to < 0:
        return node[now][start]
    else:
        visited[to] = True
        price += dfs(to)
        return price

N = int(input())
node = [[]] * N
for i in range(N):
    node[i] = list(map(int, input().split()))

result = 1000000 * N
for start in range(N):
    visited = [False] * N
    visited[start] = True
    result = min(dfs(start), result)
print(result)