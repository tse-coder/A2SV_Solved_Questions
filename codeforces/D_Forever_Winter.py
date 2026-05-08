import sys
input = sys.stdin.readline
from collections import defaultdict
t = int(input())
for _ in range(t):
    
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    lengths = defaultdict(int)

    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    for neis in graph:
        lengths[len(neis)] += 1
    
    x_y = 0
    for deg,count in lengths.items():
        if deg == 1:
            x_y = count
    x = n-1-x_y
    print(x,x_y//x)