import sys
input = sys.stdin.readline

def solve():
    from collections import defaultdict
    
    n, m = map(int, input().split())
    graph = {}
    bad = 0
    for _ in range(m):
        u, v = map(int, input().split())
        if u != v:
            graph[u] = v
            bad += 1
    visited = {}
    cycle = 0
    def dfs(node):
        nonlocal cycle
        visited[node] = 1
        for nei in graph:
            x = graph[nei]
            if visited.get(v, 0) == 0:
                dfs(v)
            
            elif visited.get(v) == 1:
                cycle+= 1
            
        visited[node] = 2
    for node in graph:
        if visited.get(node,0) == 0:
            dfs(node)

    print(bad + cycle)
t = int(input())
for _ in range(t):
    solve()