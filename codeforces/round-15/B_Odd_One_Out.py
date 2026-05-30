import sys
input = sys.stdin.readline
 
def solve():
    n = int(input().strip())
    digits = list(map(int,list(input().strip())))
    odds = (0,False)
    evens = (0,False)
    for i in range(n):
        if i % 2 == 0:
            odds = (odds[0]+1,odds[1] or digits[i]%2==1)
        if i % 2:
            evens = (evens[0]+1,evens[1] or digits[i]%2==0)
    if odds[0] > evens[0]:
        print(1 if odds[1] else 2)
    else:
        print(2 if evens[1] else 1)
 
t = int(input())
for _ in range(t):
    solve()