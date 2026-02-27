import sys
input = sys.stdin.readline
from collections import defaultdict

def solve():
    n,k = map(int, input().split())
    nums = list(map(int, input().split()))
    freq = defaultdict(int)
    l = 0
    res = 0
    for r in range(n):
        freq[nums[r]] += 1
        while len(freq) > k:
            freq[nums[l]] -= 1
            if freq[nums[l]] <= 0:
                del freq[nums[l]]
            l += 1
        res += r - l + 1
            
    print(res)
if __name__ == '__main__':
    solve()