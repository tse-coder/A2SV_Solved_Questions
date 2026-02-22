import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    print(nums[(n-1)//2])

if __name__ == '__main__':
    solve()