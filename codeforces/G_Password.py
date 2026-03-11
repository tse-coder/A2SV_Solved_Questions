import math
t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int,input().split()))
    avail = 10-len(nums)
    poss = math.factorial(avail)//(math.factorial(avail-2)*2)
    print(poss*6)
    
