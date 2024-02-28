# 미로탐색
# 1초
# N = Y ( 2 ~ 100 )
# M = X ( 2 ~ 100 )

import sys
input = sys.stdin.readline

def bfs():
    Q = []
    Q.append([0, 0])

    while Q:
        now = Q.pop(0)

        for i in range(4):
            Y = now[0] + dy[i]
            X = now[1] + dx[i]

            if X >= 0 and Y >= 0 and X < M and Y < N:
                if table[Y][X] == 1:
                    table[Y][X] += table[now[0]][now[1]]
                    Q.append([Y, X])
    return table[N - 1][M - 1]

N, M = map(int, input().split())
dy, dx = [1, 0, -1, 0], [0, 1, 0, -1]

table = []
for i in range(N):
    table.append(list(map(int, input().rstrip())))

print(bfs())