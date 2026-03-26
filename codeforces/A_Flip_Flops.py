import sys
input = sys.stdin.readline

def solve():
    n,c,k = map(int,input().split())
    nums = list(map(int,input().split()))
    nums.sort()
    for num in nums:
        if num > c:
            break
        if k > c - num:
            k -= c-num
            c += c
        else:
            c += k + num
            k = 0
    print(c)

t = int(input())
for _ in range(t):
    solve()