import sys
input = sys.stdin.readline

def solve():
    s = input().strip()
    nears = [[s[0]]]

    for i in range(1,len(s)):
        if s[i] == nears[-1][0]:
            nears[-1].append(s[i])
        else:
            nears.append([s[i]])
    single = set()
    for near in nears:
        if len(near)%2 == 1:
            single.add(near[0])
    print("".join(sorted(list(single))))

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()