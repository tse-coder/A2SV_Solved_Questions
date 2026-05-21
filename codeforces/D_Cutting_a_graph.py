import sys
input = sys.stdin.readline
from collections import defaultdict

class DSU:
    def __init__(self,n):
        self.parent = list(range(n+1))
        self.rank = [0]*(n+1)
    
    def find(self,x):
        root = x

        while root != self.parent[root]:
            root = self.parent[root]

        while x != root:
            nextx = self.parent[x]
            self.parent[x] = root
            x = nextx
        
        return root
    
    def union(self,x,y):
        rooty = self.find(y)
        rootx = self.find(x)
        if self.rank[rooty] < self.rank[rootx]:
            self.parent[rooty] = rootx
        elif self.rank[rootx] < self.rank[rooty]:
            self.parent[rootx] = rooty
        else:
            self.parent[rootx] = rooty
            self.rank[rooty]+= 1
    def isconnected(self,x,y):
        return self.find(x) == self.find(y)

def solve():
    n,m,k = map(int,input().split())
    dsu = DSU(n)
    disconnected = defaultdict(set)
    edges = []
    for _ in range(m):
        u,v = map(int,input().split())
        edges.append((u,v))
    operations = []
    for _ in range(k):
        op , x , y = input().split()
        x,y = int(x),int(y)

        if op == "cut":
            disconnected[x].add(y)
            disconnected[y].add(x)
        
        operations.append((op,x,y))
    
    for u,v in edges:
        if (not v in disconnected[u]) and (not u in disconnected[v]):
            dsu.union(u,v)
    res = []
    for op,x,y in operations[::-1]:
        if op=="cut":
            dsu.union(x,y)
        else:
            res.append("YES" if dsu.isconnected(x,y) else "NO")
    for ret in res[::-1]:
        print(ret)
            

solve()