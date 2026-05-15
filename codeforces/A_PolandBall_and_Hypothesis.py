import sys
input = sys.stdin.readline

n = int(input())

def isprime(num):
    if num<=1:
        return False
    elif num<=3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True

for k in range(1,1001):
    if not isprime(n * k + 1):
        print(k)
        break
    
