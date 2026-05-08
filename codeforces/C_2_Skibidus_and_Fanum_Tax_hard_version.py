def solve():
    n,m = map(int,input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    b.sort()
    curr = a[-1]
    i = n-2
    while i >= 0:
        if a[i] > curr:
            if b[0]-a[i] > curr:
                print("NO")
                return
            
            l,r = 0,m-1
            wanted = 0
            while l <= r:
                mid = (l+r)//2
                if b[m]-a[i] <= curr:
                    wanted = mid
                    r = mid- 1
                else:
                    l = mid + 1
            
            a[i] = b[wanted]-a[i]
                
        curr = a[i]
        i -= 1
    print("YES")
    


t = int(input())
for _ in range(t):
    solve()