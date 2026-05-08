import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    enemy = list(map(int, list(input().strip())))
    dawit = list(map(int, list(input().strip())))
    res = 0
    for i in range(len(dawit)):
        if dawit[i]:
            if not enemy[i]:
                res += 1
            elif i-1 >= 0 and enemy[i-1]:
                enemy[i-1] = 0
                res += 1
            elif i + 1 < n and enemy[i+1]:
                enemy[i+1] = 0
                res += 1
    print(res)
    
