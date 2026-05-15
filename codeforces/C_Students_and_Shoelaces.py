import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
degree = [0] * (n+1)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    degree[u] += 1
    degree[v] += 1

q = deque()

for i in range(1,n+1):
    if degree[i] == 1:
        q.append(i)

ans = 0
while q:
    s = len(q)
    ans += 1
    for _ in range(s):
        x = q.popleft()
        degree[x] = 0
        for nei in graph[x]:
            if degree[nei] > 0:
                degree[nei] -= 1

                if degree[nei] == 1:
                    q.append(nei)

print(ans)

