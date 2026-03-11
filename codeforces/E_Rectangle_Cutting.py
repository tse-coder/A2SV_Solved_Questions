t = int(input())
for _ in range(t):
    a,b = map(int,input().split())
    l = max(a,b)
    s = min(a,b)
    if s == 1:
        print("No")
        continue

    if l == s:
        if b % 2 == 1:
            print("No")
        else:
            print("Yes")
    else:
        if s*2 == l:
            if s % 2 == 1:
                print("No")
            else:
                print("Yes")
        elif s%2 == 1 and l%1 == 1:
            print("No")
        else:
            print("Yes")
        
