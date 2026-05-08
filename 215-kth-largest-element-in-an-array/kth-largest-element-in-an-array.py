class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums: return 

        piv = random.choice(nums)
        left = [x for x in nums if x > piv]
        mid = [x for x in nums if x == piv]
        right = [x for x in nums if x < piv]

        l,m = len(left),len(mid)

        if k <= l:
            return self.findKthLargest(left,k)
        elif k > l + m:
            return self.findKthLargest(right,k-l-m)
        else:
            return mid[0]

