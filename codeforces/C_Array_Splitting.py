n,k = map(int,input().split())
nums = list(map(int,input().split()))
gaps = []
total = nums[-1] - nums[0]
if k == 1:
    print(total)
else:
    for i in range(n-1):
        gaps.append(nums[i+1] - nums[i])
    gaps.sort(reverse=True)
    max_gaps = sum(gaps[:k-1])
    print(total-max_gaps)