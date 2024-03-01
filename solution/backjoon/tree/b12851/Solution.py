# 숨바꼭질 2
# 2초
# N = start ( 0 ~ 100,000 )
# K = goal ( 0 ~ 100,000 )

from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
visited = [False] * 100001
visited[K] = True

Q = deque()
Q.append((K, 0))

answer = [0, 0]
while Q:
    now, count = Q.popleft()
    visited[now] = True

    if answer[1] > 0 and answer[0] < count:
        break
    if answer[1] > 0 and now == N:
        answer[1] += 1
        continue
    elif now == N:
        answer[0] = count
        answer[1] += 1
        continue

    if now % 2 == 0:
        if not visited[now // 2]:
            Q.append((now // 2, count + 1))
    if now - 1 >= 0:
        Q.append((now - 1, count + 1))
    if now + 1 <= 100000:
        Q.append((now + 1, count + 1))

print(answer[0])
print(answer[1])
