import sys
input = sys.stdin.readline

def solve():
    n, x, k = map(int, input().split())
    s = input().strip()
    pos = count = 0
    for _ in range(k):
        if s[pos] == "L":
            x -= 1
        elif s[pos] == "R":
            x += 1
        if x == 0:
            pos = 0
            count += 1
        if pos == n-1 and x != 0:
            break
        pos += 1
    print(count)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()