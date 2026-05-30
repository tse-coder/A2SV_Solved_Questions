import sys
input = sys.stdin.readline

def solve():
    a,x,y = map(int,input().split())
    if (a > x and a > y) or (a < x and a < y):
        print("YES")
    else:
        print("NO")

t = int(input())
for _ in range(t):
    solve()