import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
letters = list(input().strip())


stack = []
for letter in letters:
    if not stack:
        stack.append(letter)
        continue
    if len(stack) % 2 == 1:
        if letter != stack[-1]:
            stack.append(letter)
    else:
        stack.append(letter)
if len(stack)%2==1:
    stack.pop()

print(n-len(stack))
print("".join(stack))