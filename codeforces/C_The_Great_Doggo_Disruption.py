import sys
input = sys.stdin.readline
from collections import Counter

n = int(input())
puppies = list(input())
pupcount = Counter(puppies)
del(pupcount["\n"])
for pup in pupcount:
    if pupcount[pup] > 1:
        print("Yes")
        break
else:
    print("No")