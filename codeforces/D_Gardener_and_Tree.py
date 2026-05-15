import sys
from collections import defaultdict,deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    input()
    n,k = map(int,input().split())
    if n == 1:
        print(0 if k else 1)
        continue

    graph = [[] for _ in range(n+1)]
    degree = [0] * (n+1)

    for _ in range(n-1):
        u,v = map(int,input().split())
        graph[v].append(u)
        graph[u].append(v)
        degree[v] += 1
        degree[u] += 1
    

    
    q = deque()

    for i in range(1,n+1):
        if degree[i] == 1:
            q.append(i)
    rem = n

    while k > 0 and q:
        s = len(q)
        rem -= s

        for _ in range(s):
            x = q.popleft()
            for nei in list(graph[x]):
                degree[nei] -= 1

                if degree[nei] == 1:
                    q.append(nei)
                    
        k -= 1
        
    print(rem)
