class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        evenSum = 0
        res = []
        for i in range(len(nums)):
            if nums[i]%2==0:
                evenSum+=nums[i]
        for query in queries:
            if nums[query[1]] % 2 == 0:
                evenSum -= nums[query[1]]
            nums[query[1]] = nums[query[1]] + query[0]
            if nums[query[1]] %2==0:
                evenSum += nums[query[1]]
            res.append(evenSum)
        return res