t = int(input())

def solve():
    l = int(input())
    nums = list(input().strip())
    # remove the right even numbers
    while nums and int(nums[-1]) % 2 == 0:
        nums.pop()

    if not nums:
        print(-1)
        return

    tot = sum([int(num) for num in nums])
    if tot % 2 == 0:
        print("".join(nums))
        return

    # if odd remove the first odd number except the last one
    for i in range(len(nums)-2,-1,-1):
        if int(nums[i]) % 2 == 1:
            nums.pop(i)
            res = "".join(nums).lstrip("0")
            print(res if res else -1)
            return

    print(-1)

for _ in range(t):
    solve()
