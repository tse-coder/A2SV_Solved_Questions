import sys
from collections import deque
input = sys.stdin.readline


t = int(input())
for _ in range(t):
    n = int(input())
    arr = [int(x) - 1 for x in input().split()]
    indeg = [0] * n

    for v in arr:
        indeg[v] += 1

    q = deque()

    for i in range(n):
        if indeg[i] == 0:
            q.append(i)

    depth = [0] * n
    while q:
        v = q.popleft()
        u = arr[v]

        depth[u] = max(depth[u],depth[v]+1)
        indeg[u] -= 1

        if indeg[u] == 0:
            q.append(u)
    print(max(depth) + 2)
    

