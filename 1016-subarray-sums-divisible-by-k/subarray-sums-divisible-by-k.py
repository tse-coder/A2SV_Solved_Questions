class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        rem_map = {0:1}
        res = 0
        acc = 0
        for num in nums:
            acc += num
            mod = acc % k
            if mod < 0:
                mod += k
            if mod in  rem_map:
                res += rem_map[mod]
                rem_map[mod] += 1
            else:
                rem_map[mod] = 1

        return res
        
        


