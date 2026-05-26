import sys
input = sys.stdin.readline

def solve():
    a, b = map(int, input().split())
    h = list(map(int, input().split()))
    dp = [0]*a
    for i in range(1,a): 
        dp[i] = min(dp[j]+abs(h[i]-h[j]) for j in range(max(0,i-b),i))
    print(dp[-1]) 
solve()