import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    dp = []
    
    for i in range(n):
        dp.append(list(map(int,input().split())))
    
    for i in range(1,n):
        dp[i][0] = dp[i][0] + max(dp[i-1][1],dp[i-1][2])
        dp[i][1] = dp[i][1] + max(dp[i-1][0],dp[i-1][2])
        dp[i][2] = dp[i][2] + max(dp[i-1][1],dp[i-1][0])
    print(max(dp[-1]))
solve()