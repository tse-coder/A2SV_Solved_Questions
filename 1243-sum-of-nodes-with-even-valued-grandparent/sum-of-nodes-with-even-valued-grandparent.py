# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(node):
            if not node:
                return 0
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            if node.val % 2 == 0:
                self.res += left_sum + right_sum
            return (
                (node.left.val if node.left else 0) +
                (node.right.val if node.right else 0)
            )
        dfs(root)
        return self.res