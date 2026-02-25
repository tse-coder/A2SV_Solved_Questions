class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        lens = []
        for val in arr:
            lens.append([bin(val).count("1"),val])
        lens.sort(key=lambda x: (x[0],x[1]))
        return [x[1] for x in lens]
        