import sys
from collections import Counter, defaultdict
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

freq = Counter(arr)

if max(freq.values()) > k:
    print("NO")
    exit()

print("YES")

pos = defaultdict(list)
for i in range(n):
    pos[arr[i]].append(i)

res = [0] * n
color = 1

for val in pos:
    for idx in pos[val]:
        res[idx] = color
        color += 1
        if color > k:
            color = 1

print(*res)