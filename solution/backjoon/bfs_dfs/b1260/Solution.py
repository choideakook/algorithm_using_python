# DFS 와 BFS
# 2초
# N = node ( 1 ~ 1,000 )
# M = 간선 ( 1 ~ 10,000 )
# V = 시작점

import sys
input = sys.stdin.readline

def dfs(now):
    dfs_visited[now] = True
    print(now, end=" ")

    for i in range(1, N + 1):
        if not dfs_visited[i] and nodes[now][i]:
            dfs(i)

def bfs():
    Q = []
    bfs_visited[V] = True
    Q.append(V)
    print()

    while Q:
        now = Q.pop(0)
        print(now, end=" ")

        for i in range(1, N + 1):
            if not bfs_visited[i] and nodes[now][i]:
                bfs_visited[i] = True
                Q.append(i)

N, M, V = map(int, input().split())

dfs_visited = [False] * (N + 1)
bfs_visited = [False] * (N + 1)
nodes = [[False] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    nodes[a][b] = True
    nodes[b][a] = True

dfs(V)
bfs()