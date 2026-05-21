import sys
input = sys.stdin.readline

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
            self.rank[rooty] += 1
    def isconnected(self,x,y):
        return self.find(x) == self.find(y)

def solve():
    n,m1,m2 = map(int,input().split())
    dsuf = DSU(n)
    dsug = DSU(n)
    edgesf = []
    edgesg = []
    res = 0
    for _ in range(m1):
        u,v = map(int,input().split())
        edgesf.append((u,v))
    for _ in range(m2):
        u,v = map(int,input().split())
        dsug.union(u,v)
        edgesg.append((u,v))
    
    for u,v in edgesf:
        if not dsug.isconnected(u,v):
            res += 1 # remove the edge in f 
        else:
            dsuf.union(u,v)
    
    for u,v in edgesg:
        if not dsuf.isconnected(u,v):
            res += 1
            dsuf.union(u,v)
    
    print(res)
t = int(input())
for _ in range(t):
    solve()