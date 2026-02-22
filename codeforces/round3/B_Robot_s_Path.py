n,k = map(int,input().split())
sectors = list(input())
max_obs = 0
count = 0
for i in range(n):
    if sectors[i] == ".":
        
        count = 0
    else:
        count += 1
    max_obs = max(max_obs,count)
if max_obs >= k:
    print("NO")
else:    
    print("YES")