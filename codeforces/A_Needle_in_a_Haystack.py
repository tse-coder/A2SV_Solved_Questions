from bisect import bisect_left
from collections import Counter
import sys
input = sys.stdin.readline

def solve():
    s = input().strip()
    t = input().strip()
    s_dict = Counter(s)
    t_dict = Counter(t)

    diff = []
    for char in s_dict:
        if char not in t_dict:
            print("Impossible")
            return

    for char in t_dict:
        if char not in s_dict:
            diff.extend([char] * t_dict[char])
        elif s_dict[char] < t_dict[char]:
            diff.extend([char] * (t_dict[char] - s_dict[char]))

    diff.sort()
    sp , tp = 0, 0
    res = []

    while sp < len(s) and tp < len(diff):
        if s[sp] > diff[tp]:
            res.append(diff[tp])
            tp += 1
        else:
            res.append(s[sp])
            sp += 1

    res.extend([diff[i] for i in range(tp,len(diff))])
    res.extend([s[i] for i in range(sp,len(s))])

    print("".join(res))

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()
