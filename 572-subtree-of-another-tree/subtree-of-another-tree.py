class Solution:
    def equal(self, root, node2):
        if not root and not node2:
            return True
        if not root or not node2:
            return False
        if root.val != node2.val:
            return False
        
        return (
            self.equal(root.left, node2.left) and
            self.equal(root.right, node2.right)
        )

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        if self.equal(root, subRoot):
            return True
        
        return (
            self.isSubtree(root.left, subRoot) or
            self.isSubtree(root.right, subRoot)
        )