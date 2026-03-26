import sys
input = sys.stdin.readline

def solve():
    s = input().strip()
    if "><" in s.replace("*",""):
        print(-1)
        return
    left = 0
    while s[left] == "<" and left < len(s):
        left += 1

    i = len(s) -1
    right = 0
    while s[i] == ">" and i >= 0:
        right += 1
        i -= 1
    
    print(max(right,left))

t = int(input())
for _ in range(t):
    solve()