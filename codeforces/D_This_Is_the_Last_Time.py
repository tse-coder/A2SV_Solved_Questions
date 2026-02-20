t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int,input().split())))
    matrix.sort()
    for val in matrix:
        if k > val[2]:
            continue
        elif val[0] <= k:
            k = val[2]
        else:
            break
    print(k)