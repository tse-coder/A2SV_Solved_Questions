import sys
input = sys.stdin.readline

def solve():
    n,m = map(int,input().split())
    str1 = input().strip()
    str2 = input().strip()
    
    for i in range(n-m):
        incs = 0
        decs = 0
        for j in range(m):
            if ord(str2[j]) > ord(str1[j+i]):
                incs += abs(ord(str2[j])-ord(str1[j+i]))
            else: 
                decs += abs(ord(str2[j])-ord(str1[j+i]))
        if abs(incs-decs) <= 1:
            print("YES")
            break
    else:
        print("NO")

t = int(input())
for _ in range(t):
    solve()

    
