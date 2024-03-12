# 케빈 베이컨의 6단계 법칙
# 2초

# N = users ( 2 ~ 100 )
# M = relationship ( 1 ~ 5,000 )

from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    visited = [False] * (N + 1)
    Q = deque()
    Q.append((start, 0))
    visited[start] = True

    result = 0
    while Q:
        now, term = Q.popleft()
        result += term

        for i in node[now]:
            if not visited[i]:
                visited[i] = True
                Q.append((i, term + 1))
    return result

N, M = map(int, input().split())

node = []
for i in range(N + 1):
    node.append(set())

for _ in range(M):
    a, b = map(int, input().split())
    node[a].add(b)
    node[b].add(a)

num, count = 0, N * M
for start in range(1, N + 1):
    result = bfs(start)
    if result < count:
        num, count = start, result
print(num)