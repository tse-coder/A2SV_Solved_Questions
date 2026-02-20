t = int(input())
for _ in range(t):
    n = int(input())
    letters = input()
    pos = ["aa","aab","baa","aba","aac","caa","aca"]
    for val in pos:
        if val in letters:
            print(len(val))
            break
    else:
        print(-1)