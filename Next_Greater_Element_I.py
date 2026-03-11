class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_map = defaultdict(lambda: -1)
        for num in nums2:
            while stack and stack[-1] < num:
                next_map[stack.pop()] = num
            stack.append(num)

        return [next_map[num] for num in nums1]
