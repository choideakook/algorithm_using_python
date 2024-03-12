# 퍼즐
# 1초

from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    dy, dx = [1, 0, -1, 0], [0, 1, 0, -1]
    Q = deque()
    visited = {}
    Q.append(start)
    visited[start] = 0

    while Q:
        now = Q.popleft()
        if now == "123456789":
            return visited[now]

        blank = now.find("9")
        y = blank // 3
        x = blank % 3

        for i in range(4):
            Y = y + dy[i]
            X = x + dx[i]

            if 0 <= X < 3 and 0 <= Y < 3:
                target = Y * 3 + X
                next = now.replace("9", now[target])
                next = next[:target] + "9" + next[target + 1:]

                if next not in visited:
                    visited[next] = visited[now] + 1
                    Q.append(next)
    else: return -1

start = ""
for i in range(3):
    start += input().strip()

start = (start
         .replace(" ", "")
         .replace("0", "9"))
print(bfs())
