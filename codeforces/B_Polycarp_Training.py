import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    count = 0
    for i in range(n):
        if nums[i] > count:
            count += 1
    print(count)

if __name__ == '__main__':
    solve()