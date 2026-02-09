class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countDict = {}
        for num in nums:
            if num in countDict:
                countDict[num]+=1
            else:
                countDict[num] = 1
        pair = []
        for val in countDict:
            pair.append([countDict[val],val])
        pair.sort()
        res = []
        for i in range(len(pair)-1,len(pair)-1-k,-1):
            res.append(pair[i][1])
        return res
