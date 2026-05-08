import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(n):
        for j in range(i+1,n):
            if arr[i] == j+1 and arr[j] == i+1:
                print(2)
                return
    print(3)

t = int(input())
for _ in range(t):
    solve()
