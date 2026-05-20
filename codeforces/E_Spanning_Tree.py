import sys
input = sys.stdin.readline
 
class DSU:
    def __init__(self,size):
        self.parent = list(range(size+1))
        self.rank = [0] * (size+1)
    
    def find(self,x):
        root = x
        while root != self.parent[root]:
            root=self.parent[root]
        
        # path compresion
        while x != root:
            nextx = self.parent[x]
            self.parent[x] = root
            x = nextx
        
        return root
    
    def union(self,x,y):
        rootx = self.find(x)
        rooty = self.find(y)
        if self.rank[rootx] > self.rank[rooty]:
            self.parent[rooty] = rootx
        elif self.rank[rooty] > self.rank[rootx]:
            self.parent[rootx] = rooty
        else:
            self.parent[rootx] = rooty
            self.rank[rooty] += 1
 
def solve():
    n, m = map(int, input().split())
    edges = []
    
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((w,u,v))
    
    edges.sort()
    dsu = DSU(n)
    weight = 0
    for w,u,v in edges:
        if dsu.find(u) != dsu.find(v):
            dsu.union(u,v)
            weight += w
    print(weight)
 
solve() 