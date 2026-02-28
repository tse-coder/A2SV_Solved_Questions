import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int,list(input().strip())))
    b = list(map(int,list(input().strip())))
    ones = a.count(1)
    zeros = a.count(0)

    invert = 0
    for i in range(n-1,-1,-1):
        if a[i]^invert != b[i]: 
            #invert
            if zeros != ones:
                print("NO")
                return
            invert ^= 1

        if a[i] == 0:
            zeros -= 1
        else:
            ones -= 1
    print("YES")
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()