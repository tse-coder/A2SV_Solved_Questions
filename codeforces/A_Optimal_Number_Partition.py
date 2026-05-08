import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr.sort()
res = 0
l,r = 0,len(arr)-1
while l < r:
    res += (arr[l] + arr[r])**2
    l += 1
    r -= 1
print(res)
