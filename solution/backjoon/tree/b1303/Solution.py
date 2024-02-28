# 전투
# 2초
# N = rows ( 1 ~ 100 )
# M = cols ( 1 ~ 100 )

import sys
input = sys.stdin.readline

def dfs(now, color):
    visited[now[0]][now[1]] = True
    count = 1

    for i in range(4):
        Y = now[0] + dy[i]
        X = now[1] + dx[i]

        if X >= 0 and Y >= 0 and X < N and Y < M:
            if not visited[Y][X] and color == table[Y][X]:
                count += dfs([Y, X], color)
    return count

N, M = map(int, input().split())

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
visited = [[False] * N for _ in range(M)]
table, answer = [], [0, 0]

for i in range(M):
    table.append(list(input().strip()))

for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            count = dfs([i, j], table[i][j])
            if table[i][j] == "W":
                answer[0] += (count * count)
            else:
                answer[1] += (count * count)

print(*answer)
