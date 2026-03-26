import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def canForm(n,m):
    if n == m:
        return True
    if n < m:
        return False
    if n % 3 != 0:
        return False
    return canForm(n//3,m) or canForm((n//3)*2,m)


def solve():
    n,m = map(int,input().split())
    if canForm(n,m):
        print("YES")
    else:
        print("NO")

t = int(input())
for _ in range(t):
    solve()