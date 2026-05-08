import sys
input = sys.stdin.readline

def solve():
    a,b = map(int,input().split())
    best = 10**9
    for add in range(0, 100):
        bb = b + add
        if bb == 1:
            continue
        cnt = add
        x = a
        while x > 0:
            x //= bb
            cnt += 1
        if cnt < best:
            best = cnt
    print(best)


t = int(input())
for _ in range(t):
    solve()