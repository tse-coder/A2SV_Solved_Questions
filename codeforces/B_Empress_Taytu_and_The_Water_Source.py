import sys
input = sys.stdin.readline
from math import ceil

t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    ds = list(map(int, input().split()))
    hrs = list(map(int,input().split()))
    if sum(hrs) > k:
        print(-1)
        continue

    l,r = 1,max(ds)
    res = r
    while l <= r:
        m = (l+r)//2
        tot = 0
        for i,d in enumerate(ds):
            tot += ceil(d/m)*hrs[i]

        if tot <= k:
            res = m
            r = m-1
        else:
            l = m+1
    print(res)
    
