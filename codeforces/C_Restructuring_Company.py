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
    n, k = map(int, input().split())
    dsu = DSU(n)
    for _ in range(k):
        op,x,y = map(int,input().split())
        if op == 3:
            print("YES" if dsu.isconnected(x,y) else "NO")
        elif op == 1:
            dsu.union(x,y)
        else:
            for i in range(x+1,y+1):
                dsu.union(x,i)

solve()