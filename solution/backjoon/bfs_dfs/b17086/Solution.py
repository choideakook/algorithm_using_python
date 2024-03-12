# 아기상어2
# 2초
# N = Y ( 2 ~ 50 )
# M = X ( 2 ~ 50 )

from collections import deque
import sys
input = sys.stdin.readline

dy = [1, 0, -1, 0, 1, 1, -1, -1]
dx = [0, 1, 0, -1, 1, -1, 1, -1]
N, M = map(int, input().split())

Q = deque()
table = [[0] * M for _ in range(N)]
for y in range(N):
    arr = list(map(int, input().split()))
    for x in range(M):
        if arr[x] == 1:
            table[y][x] = 1
            Q.append([y, x])

answer = 0
while Q:
    now = Q.popleft()
    answer = max(table[now[0]][now[1]], answer)

    for i in range(8):
        Y = now[0] + dy[i]
        X = now[1] + dx[i]

        if Y >= 0 and X >= 0 and Y < N and X < M:
            if table[Y][X] == 0:
                table[Y][X] += table[now[0]][now[1]] + 1
                Q.append([Y, X])
print(answer - 1)