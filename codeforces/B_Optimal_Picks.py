import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    a,b = 0,0

    i = n - 2
    while i >= 0 and k > 0:
        diff = min(k,arr[i+1]-arr[i])
        arr[i] += diff
        if k >= diff:
            k -= diff
        i -= 2
   
    while arr:
        a += arr.pop()
        if arr:
            b += arr.pop()
    print(a-b)


    
