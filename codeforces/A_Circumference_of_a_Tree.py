import sys
input = sys.stdin.readline
from collections import defaultdict

n= int(input())
graph = defaultdict(list)
visited = set()

def solve():
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

    return dfs(0,1)

def dfs(h,node):
    global visited
    for nei in graph[node]:
        if nei not in visited:
            visited.add(nei)
            dfs(h+1,nei)
    else:
        return h
if n == 1:
    print(0)
    exit()
for _ in range(n):
    solve()
