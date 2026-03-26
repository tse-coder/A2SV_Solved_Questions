n,k = map(int,input().split())
letters  = list(input())

letters = [ord(let) - ord('a') + 1 for let in letters]

letters.sort()
def solve():
    curr = [letters[0]]
    for r in range(n):
        if letters[r] - curr[-1] >= 2:
            curr.append(letters[r])
    if len(curr) < k:
        print(-1)
    else:
        print(sum(curr[:k]))
solve()