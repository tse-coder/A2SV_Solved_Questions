t = int(input())
for _ in range(t):
    nums = input().split()
    ref = int(nums[0])
    for num in nums[1:]:
        if int(num) != ref:
            print("No")
            break
    else:
        print("Yes")