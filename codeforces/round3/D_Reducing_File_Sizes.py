n,m = map(int,input().split())
files = []
total = 0
for _ in range(n):
    o,c = map(int,input().split())
    diff = o - c
    if diff > 0:
        files.append(diff)
    total += o
files.sort(reverse=True)
count = 0
for dif in files:
    if total <= m:
        break
    total -= dif
    count += 1
if total <= m:
    print(count)
else:
    print(-1)

