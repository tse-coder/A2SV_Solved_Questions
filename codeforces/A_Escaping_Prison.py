import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n,h = map(int,input().split())
    tot = 0
    for _ in range(n):
        x,y = map(int, input().split())
        tot += max(x,y)
    if tot >= h:
        print("YES")
    else:
        print("NO")
    
