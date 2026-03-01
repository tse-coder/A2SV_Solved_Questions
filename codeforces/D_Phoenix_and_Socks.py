import sys
from collections import Counter
input = sys.stdin.readline

def solve():
    n,l,r = map(int, input().split())
    nums = list(map(int, input().split()))
    lc = Counter(nums[:l])
    rc = Counter(nums[l:])
    
    res = 0
    # remove the matched pairs
    for char in list(lc.keys()):
        if char in rc:
            m = min(lc[char],rc[char])
            lc[char] -= m
            rc[char] -= m
            l -= m
            r -= m
    # make sure left side is heavier
    if l < r:
        r,l = l,r
        lc,rc = rc,lc
    # count the extra pairs in the left
    for color in lc:
        while lc[color] >= 2 and l > r:
            lc[color] -= 2
            l -= 2
            res += 1

    # flip the remaining
    rem = (l-r)//2
    res += rem
    l -= rem * 2

    
    res += l
    print(res)


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()