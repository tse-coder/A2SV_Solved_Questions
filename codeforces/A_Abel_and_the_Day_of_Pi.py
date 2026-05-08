import sys
input = sys.stdin.readline

t = int(input())
pi = "314159265358979323846264338327"
for _ in range(t):
    num = input()
    count = 0
    for i in range(len(pi)):
        if num[i] != pi[i] or i >= len(num):
            break
        count += 1
    print(count)
    
