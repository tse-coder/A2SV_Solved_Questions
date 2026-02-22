t = int(input())
books = []
for _ in range(t):
    h,w = map(int,input().split())
    books.append((h,w))
    
curr = max(books[0])
for i in range(1,t):
    h,w = books[i]
    if max(h,w) <= curr:
        curr = max(h,w)
    elif min(h,w) <= curr:
        curr = min(h,w)
    else:
        print("NO")
        break
else:
    print("YES")