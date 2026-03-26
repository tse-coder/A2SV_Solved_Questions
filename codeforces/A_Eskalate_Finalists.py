import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))

_max = max(nums)

print(_max - 25 if _max > 25 else 0)