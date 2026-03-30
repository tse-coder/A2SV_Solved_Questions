# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        def maxsum(node):
            if not node:
                return 0,True, -float("inf"), float("inf")
            
            lsum, lbst, lmax, lmin = maxsum(node.left)
            rsum, rbst, rmax, rmin = maxsum(node.right)

            if rbst and lbst and lmax < node.val < rmin:
                newsum = lsum + node.val + rsum
                self.result = max(newsum,self.result)
                return newsum, True, max(rmax,node.val), min(lmin,node.val)
            return 0, False, -float("inf"), float("inf")
        maxsum(root)
        return self.result