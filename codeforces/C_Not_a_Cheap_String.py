t = int(input())
def price(char):
    return ord(char) - ord("a") + 1
def solve():
    s = input().strip()
    n = int(input())
    acc = 0
    indexes = []
    for i,c in enumerate(s):
        acc += price(c)
        indexes.append([c,i])

    indexes.sort()
    while acc > n:
        if indexes:
            acc -= price(indexes[-1][0])
            indexes.pop()
        else:
            print("")
            return

    indexes.sort(key=lambda x: x[1])
    print("".join(index[0] for index in indexes))
for _ in range(t):
    solve()
