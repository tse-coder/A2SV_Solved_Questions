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
            self.rank[rooty]+= 1

def solve():
    n,m,k = map(int,input().split())
    dsu = DSU(n)
    for _ in range(m):
        u,v = map(int,input().split())
        dsu.union(u,v)
    
    for _ in range(k):
        op , x , y = input().split()
        if op == "ask":
            print("YES" if dsu.find(int(x)) == dsu.find(int(y)) else "NO")
        if op == "cut":
            rootx = dsu.find(int(x))
            rooty = dsu.find(int(y))
            if rooty == rootx:
                dsu.parent[int(x)] = int(x)
solve()