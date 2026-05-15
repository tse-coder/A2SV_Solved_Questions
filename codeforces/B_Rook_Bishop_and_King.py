r1,c1,r2,c2 = map(int,input().split())

def solve():
    # rook
    r = 0
    if r1 == r2 or c1 == c2:
        r = 1
    else:
        r = 2

    # bishop
    b = 0
    if abs(r1-r2) == abs(c1-c2):
        b = 1
    elif (abs(r1-r2) + abs(c1-c2)) % 2 == 0:
        b = 2

    # king
    k = max(abs(r1-r2),abs(c1-c2))
    print(r,b,k)

if (r1,c1) == (r2,c2):
    print(0,0,0)
else:
    solve()
