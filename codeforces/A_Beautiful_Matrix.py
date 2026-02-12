matrix = []
index = [0,0]
for i in range(5):
    curr = list(map(int,input().split()))
    matrix.append(curr)
    for j in range(len(curr)):
        if curr[j] == 1:
            index = [i,j]
            break
print(abs(index[0]-2)+abs(index[1]-2))