import sys
input = sys.stdin.readline

s1 = input().strip()
s2 = input().strip()
total = 0
for char in s1:
    if char == "+":
        total+=1
    else:
        total-=1

similar = 0
all = 0

def score(i,curr):
    global all, similar
    if i == len(s1):
        if curr == total:
            similar += 1
        all += 1
        return
    
    if s2[i] == "?":
        score(i+1,curr+1)
        score(i+1,curr-1)
    elif s2[i] == "-":
        score(i+1,curr-1)
    else:
        score(i+1,curr+1)

score(0,0)
print(similar/all)