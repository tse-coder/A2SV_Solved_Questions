import sys
input = sys.stdin.readline
from collections import Counter

def solve():
    s = list(input().strip())
    t = list(input().strip())
    p = list(input().strip())

    # check if it's a subsequence
    i = 0
    for char in t:
        if i < len(s) and s[i] == char:
            i += 1

    if i != len(s):
        print("NO")
        return

    joined = s + p
    jc = Counter(joined)
    tc = Counter(t)
    
    for char in tc:
        if char not in jc:
            print("NO")
            return
        if jc[char] < tc[char]:
            print("NO")
            return
    print("YES")
t = int(input())
for _ in range(t):
    solve()