import sys
input = sys.stdin.readline
n = int(input().strip())
queenx,queeny = map(int,input().split())
kingx,kingy = map(int,input().split())
destx,desty = map(int,input().split())

if ((kingx<queenx and destx<queenx or kingx>queenx and destx>queenx)and
   (kingy>queeny and desty>queeny or kingy<queeny and desty<queeny)):
    print("YES")
else:
    print("NO")