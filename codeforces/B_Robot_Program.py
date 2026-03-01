import sys
input = sys.stdin.readline

def solve():
    n, x, k = map(int, input().split())
    s = input().strip()
    
    pref = []
    cur = 0
    
    for c in s:
        if c == 'L':
            cur -= 1
        else:
            cur += 1
        pref.append(cur)

    first_hit = -1
    for i in range(n):
        if x + pref[i] == 0:
            first_hit = i + 1
            break
    
    if first_hit == -1 or first_hit > k:
        print(0)
        return
    
    ans = 1
    remaining = k - first_hit
    

    cycle = -1
    for i in range(n):
        if pref[i] == 0:
            cycle = i + 1
            break
    
    if cycle != -1:
        ans += remaining // cycle
    
    print(ans)


t = int(input())
for _ in range(t):
    solve()