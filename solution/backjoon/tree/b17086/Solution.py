# 아기상어2
# 2초
# N = Y ( 2 ~ 50 )
# M = X ( 2 ~ 50 )

from collections import deque
import sys
input = sys.stdin.readline

def bfs(index):
    visited = [[False] * M for _ in range(N)]
    visited[index[0]][index[1]] = True
    Q = deque()
    Q.append((index, 1))

    while Q:
        now, count = Q.popleft()

        for i in range(8):
            Y = now[0] + dy[i]
            X = now[1] + dx[i]

            if Y >= 0 and X >= 0 and Y < N and X < M:
                if table[Y][X] == 1:
                    return count
                elif not visited[Y][X]:
                    visited[Y][X] = True
                    Q.append(([Y, X], count + 1))

    return count

dy = [1, 0, -1, 0, 1, 1, -1, -1]
dx = [0, 1, 0, -1, 1, -1, 1, -1]
N, M = map(int, input().split())
table = []
for i in range(N):
    table.append(list(map(int, input().split())))

answer = 0
for y in range(N):
    for x in range(M):
        if table[y][x] == 0:
            answer = max(bfs([y, x]), answer)
print(answer)