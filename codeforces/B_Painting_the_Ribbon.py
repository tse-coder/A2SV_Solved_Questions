import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n,m,k = map(int,input().split())
    rem = 0
    if (n//m*m) < n:
        rem = 1
    if((n - (n//m) - rem) > k):
        print("YES")
    else:
        print("NO")
    
