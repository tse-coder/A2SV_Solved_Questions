import sys
input = sys.stdin.readline

def solve():
    M = 200000
    n,k,q = map(int,input().split())
    sug = [0]*(M+2)
    for _ in range(n):
        a, b = map(int, input().split())
        sug[a] += 1
        sug[b+1] -= 1
    
    for i in range(1,M+2):
        sug[i] = sug[i-1] + sug[i]
    
    pref = [0]*(M+2)

    for i in range(1,(M+2)):
        pref[i] = pref[i-1]
        if sug[i] >= k:
            pref[i] += 1
    
    for _ in range(q):
        x,y = map(int,input().split())
        print(pref[y] - pref[x-1])
solve()