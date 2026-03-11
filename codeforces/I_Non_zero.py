t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int,input().split()))
    tot = 0
    res = 0
    for num in nums:
        if num == 0:
            res += 1
            tot += 1
        else:
            tot += num
    if tot == 0:
        print(res+1)
    else:
        print(res)
    