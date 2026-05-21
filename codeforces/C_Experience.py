class DSU:
    def __init__(self,n):
        self.parent = list(range(n+1))
        self.rank = [0]*(n+1)
        self.experience = [0]*(n+1)

    def find(self,x):
        if self.parent[x] != x:
            p = self.parent[x]
            self.parent[x] = self.find(p)
            self.experience[x] += self.experience[p]

        return self.parent[x]

    def union(self,x,y):
        rooty = self.find(y)
        rootx = self.find(x)

        if self.rank[rooty] < self.rank[rootx]:
            self.parent[rooty] = rootx
            self.experience[rooty] -= self.experience[rootx]
        elif self.rank[rootx] < self.rank[rooty]:
            self.parent[rootx] = rooty
            self.experience[rootx] -= self.experience[rooty]
        else:
            self.parent[rootx] = rooty
            self.experience[rootx] -= self.experience[rooty]
            self.rank[rooty] += 1

    def add(self,x,v):
        rootx = self.find(x)
        self.experience[rootx] += v

n,m = map(int,input().split())
dsu = DSU(n)
for _ in range(m):
    operations = input().strip().split()
    if len(operations) > 2:
        op = operations[0]
        x,y = int(operations[1]),int(operations[2])
        if op == "add":
            dsu.add(x,y)
        else:
            dsu.union(x,y)
    else:
        x = int(operations[1])
        dsu.find(x)
        print(dsu.experience[x])
