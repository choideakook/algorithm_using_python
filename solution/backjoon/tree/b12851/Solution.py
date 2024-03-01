# 숨바꼭질 2
# 2초
# N = start ( 0 ~ 100,000 )
# K = goal ( 0 ~ 100,000 )

from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
visited = [0] * 100001

Q = deque()
Q.append(N)

answer = [0, 0]
while Q:
    now = Q.popleft()

    if now == K:
        answer[0] = visited[now]
        answer[1] += 1
        continue

    for i in [now + 1, now - 1, now * 2]:
        if answer[1] > 0 and answer[0] <= visited[now]:
            break
        if 0 <= i <= 100000 and (visited[i] == 0 or visited[i] == visited[now] + 1):
            visited[i] = visited[now] + 1
            Q.append(i)

print(answer[0])
print(answer[1])
