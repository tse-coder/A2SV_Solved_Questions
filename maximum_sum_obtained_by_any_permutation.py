
class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        freqs = [0]*len(nums)
        MOD = 10**9 + 7
        for request in requests:
            freqs[request[0]] += 1
            if request[1] < len(nums)-1:
                freqs[request[1]+1] -= 1

        for i in range(1,len(freqs)):
            freqs[i] += freqs[i-1]

        freqs.sort()
        nums.sort()
        res = 0
        for i in range(len(freqs)):
            res = (res + freqs[i] * nums[i])%MOD
    
        return res