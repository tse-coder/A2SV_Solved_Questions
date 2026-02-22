import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    string = input()
    res = float('inf')
    if len(string) < 2:
        print(-1)
        return
    for i in range(n-1):
        a = b = c = 0
        for j in range(i,min(n, i+7)):
            if string[j] == 'a':
                a += 1
            elif string[j] == 'b':
                b += 1
            else:
                c += 1
            if a > b and a > c and j - i + 1 >= 2:
                res = min(res, j - i + 1)
    print(-1 if res == float('inf') else res)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()