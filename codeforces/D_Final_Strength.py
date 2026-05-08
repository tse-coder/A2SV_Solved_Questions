import sys
input = sys.stdin.readline

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = (len(arr))//2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    print(end="")
    return merge(left,right)

def merge(left,right):
    l,r = 0,0
    ans = []
    while l < len(left) and r < len(right):
        if left[l][1] > right[r][1]:
            left[l][1] += len(right) - r
            ans.append(left[l])
            l += 1
        elif right[r][1] > left[l][1]:
            right[r][1] += len(left) - l
            ans.append(right[r])
            r += 1
        else:
            ans.append(left[l])
            l += 1
    while l < len(left):
        ans.append(left[l])
        l += 1
    while r < len(right):
        ans.append(right[r])
        r += 1
    print(ans)
    return ans

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    enum = [[i,val] for i , val in enumerate(arr)]
    sorted_enum = mergeSort(enum)
    sorted_enum.sort(key=lambda x: x[0])
    print(*[x[1] for x in sorted_enum])
