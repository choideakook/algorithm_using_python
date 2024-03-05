# 토마토
# 1초
# M = X ( 2 ~ 1,000 )
# N = Y ( 2 ~ 1,000 )

from collections import deque
import sys
input = sys.stdin.readline

dy, dx = [1, 0, -1, 0], [0, 1, 0, -1]
M, N = map(int, input().split())

Q = deque()
table = [[0] * M for _ in range(N)]
for y in range(N):
    arr = list(map(int, input().split()))
    for x in range(M):
        table[y][x] = arr[x]
        if arr[x] == 1:
            Q.append([y, x])

d_day = 0
while Q:
    now = Q.popleft()

    for i in range(4):
        Y = now[0] + dy[i]
        X = now[1] + dx[i]

        if 0 <= Y < N and 0 <= X < M:
            if table[Y][X] == 0:
                table[Y][X] = table[now[0]][now[1]] + 1
                Q.append([Y, X])
                d_day = max(table[Y][X], d_day)
def d_day_count(d_day):
    for y in range(N):
        for x in range(M):
            if table[y][x] == 0:
                return -1
    return max(d_day, 0)
print(d_day_count(d_day - 1))