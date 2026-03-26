import sys
input = sys.stdin.readline

n,k = map(int,input().split())
nums = list(map(int,input().split()))

l = 0
_max = _min = nums[0]

for r in range(n):
    if nums[r] - nums[l] >= k:
        l += 1
    else:
        _min = min(_min,nums[r])
        _max = max(_max,nums[r])
    