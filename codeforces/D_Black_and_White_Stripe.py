import sys
input = sys.stdin.readline

def solve():
    n,k = map(int, input().split())
    s = input().strip()
    
    whites = s[:k].count("W")
    if n == k:
        print(whites)
        return
    l = 0
    res = whites
    for r in range(k,n):
        if s[r] == "W":
            whites += 1
        if s[l] == "W":
            whites -= 1
        res = min(whites,res)
        l += 1
    print(res)
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()