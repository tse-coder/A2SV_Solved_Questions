import sys
input = sys.stdin.readline
from collections import Counter

n = int(input())
nums = list(map(int, input().split()))

arr = sorted(nums)
rank = dict()
curr_rank = 1
for num in arr[::-1]:
    if num not in rank:
        rank[num] = curr_rank
    curr_rank += 1

print(*[rank[num] for num in nums])