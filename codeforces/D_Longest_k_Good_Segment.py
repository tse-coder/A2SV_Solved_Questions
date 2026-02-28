import sys
from collections import defaultdict
input = sys.stdin.readline

def solve():
    n,k = map(int, input().split())
    nums = list(map(int, input().split()))
    nums_dict = defaultdict(int)
    l = 0
    res = [1,1]
    for r in range(n):
        nums_dict[nums[r]] += 1
        while len(nums_dict) > k:
            nums_dict[nums[l]] -= 1
            if nums_dict[nums[l]] == 0:
                del nums_dict[nums[l]]
            l += 1
        
        if r - l > res[1] - res[0]:
            res = [l+1,r+1]
    print(*res)
if __name__ == '__main__':
    solve()