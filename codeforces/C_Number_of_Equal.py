import sys
from collections import Counter
input = sys.stdin.readline


def solve():
    n,m = map(int, input().split()) 
    nums1 = list(map(int, input().split()))
    nums2 = list(map(int, input().split()))
    c2 = Counter(nums2)
    res = 0
    for char in nums1:
        res += c2[char]
    print(res)
        
if __name__ == '__main__':
    solve()