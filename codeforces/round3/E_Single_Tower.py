t = int(input())
s, c = 0, 0
towers  = []
final = []

for _ in range(t):
    nums = list(map(int,input().split()))
    tower = nums[1:]
    towers.append(tower)
    final.extend(tower)
final.sort()

nex = dict()

for i in range(len(final)-1):
    nex[final[i]] = final[i+1]

nex[final[-1]] = -1

for tower in towers:
    for i in range(len(tower)-1):
        if tower[i+1] != nex[tower[i]]:
            s += 1
            t += 1
c = t - 1
print(s, c)
