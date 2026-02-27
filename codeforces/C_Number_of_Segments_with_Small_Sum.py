import sys
input = sys.stdin.readline

def solve():
    n,s = map(int, input().split())
    nums = list(map(int, input().split()))
    r = 0
    tot = 0
    curr_sum = 0
    for l in range(n):
        while r < n and curr_sum + nums[r] <= s:
            curr_sum += nums[r]
            r += 1
        
        tot += r - l
        curr_sum -= nums[l]
    print(tot)

if __name__ == '__main__':
    solve()