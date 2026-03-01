import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math
 
# input = input
input = sys.stdin.readline
 
def bubble(nums, k):
    swaps = []
    for i in range(len(nums)):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j + 1] , nums[j] = nums[j] , nums[j + 1]
                swaps.append((k , j + 1))
    return (nums, swaps)
 
def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    swaps  = [] # store tuples
    a , s = bubble(a, 1)
    swaps.extend(s)
    b , s = bubble(b, 2)
    swaps.extend(s)
    for i in range(n):
        if a[i] > b[i]:
            swaps.append((3, i + 1))
    print(len(swaps))
    for s in swaps:
        print(*s)
 
 
 
def main():
    t = int(input())
    
    for _ in range(t):
        solve()
 
 
if __name__ == '__main__':
    main()