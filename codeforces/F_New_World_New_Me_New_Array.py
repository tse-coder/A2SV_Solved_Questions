t = int(input())
for _ in range(t):
    n,k,p = map(int,input().split())
    if n*p < abs(k):
        print(-1)
        continue
    if abs(k) % p == 0:
        print(abs(k)//p)
    else:
        print(abs(k)//p + 1)