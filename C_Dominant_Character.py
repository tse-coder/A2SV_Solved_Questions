n = int(input())
for _ in range(n):
    n = int(input())
    s = input()
    subs = s.split("a")
    if len(subs) ===
    if len(subs 2:
        print(-1)
    else:
        min_len = min(len(sub) for sub in subs)
        print(min_len+2)
        