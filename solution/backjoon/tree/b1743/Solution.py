# 음식물 피하기
# 2초
# N = Y ( 1 ~ 100 )
# M = X ( 1 ~ 100 )
# K = target ( 1 ~ N * M )

import sys
input = sys.stdin.readline

def dfs(now):
    count = 1
    table[now[0]][now[1]] = False

    for i in range(4):
        Y = now[0] + dy[i]
        X = now[1] + dx[i]

        if Y >= 0 and X >= 0 and Y < N and X < M:
            if table[Y][X]:
                count += dfs([Y, X])
    return count

dy, dx = [1, 0, -1, 0], [0, 1, 0, -1]
N, M, K = map(int, input().split())
table = [[False] * M for _ in range(N)]

for i in range(K):
    r, c = map(int, input().split())
    table[r - 1][c - 1] = True

answer = 0
for r in range(N):
    for c in range(M):
        if table[r][c]:
            answer = max(answer, dfs([r, c]))

print(answer)