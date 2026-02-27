
import sys
input = sys.stdin.readline

def solve():
    n,s = map(int, input().split())
    nums = list(map(int, input().split()))
    count = 0
    curr_sum = 0
    r = 0
    for l in range(n):
        while curr_sum < s and r < n:
            curr_sum += nums[r]
            r += 1
        if curr_sum >= s:
            count += n - r + 1
        curr_sum -= nums[l]
        
    print(count)

if __name__ == '__main__':
    solve()