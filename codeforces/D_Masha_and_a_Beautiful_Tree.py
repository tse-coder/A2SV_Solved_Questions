import sys
input = sys.stdin.readline

def merge(arr):
    if len(arr) == 2:
        s = sorted(arr)
        if s == arr:
            return 0,s,True
        else:
            return 1,s,True
    mid = len(arr) // 2
    l = arr[:mid]
    r = arr[mid:]
    l_cnt, l_arr, l_ok = merge(l)
    r_cnt, r_arr, r_ok = merge(r)
    if l_arr[-1] > r_arr[0] and l_arr[0] < r_arr[-1]:
        return 0,[],False
    

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
