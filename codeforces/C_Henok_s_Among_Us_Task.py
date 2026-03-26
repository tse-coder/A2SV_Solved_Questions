import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

a,b = map(int,input().split())

stack = [b]

def canConvert(n):

    if n == a:
        return True
    elif n < a:
        return False
    
    if n % 10 == 1:
        stack.append(n//10)
        return canConvert(n//10)
    elif n % 2 == 0:
        stack.append(n//2)
        return canConvert(n//2)
    else:
        return False

can_convert = canConvert(b)
print("YES" if can_convert else "NO")
if can_convert:
    print(len(stack))
    print(*stack[::-1])