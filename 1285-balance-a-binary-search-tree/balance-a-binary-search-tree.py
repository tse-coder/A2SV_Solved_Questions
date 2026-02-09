# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # generate a sorted array out of it 
        inorderArr = []
        def inorder(node,arr):
            if node == None:
                return 
            inorder(node.left,arr)
            arr.append(node.val)
            inorder(node.right,arr)
        inorder(root,inorderArr)
        # generate the tree
        def array_to_tree(arr):
            if not arr:
                return None
            mid = len(arr)//2
            node = TreeNode(arr[mid])
            node.left = array_to_tree(arr[:mid])
            node.right = array_to_tree(arr[mid+1:])   
            return node  
        return array_to_tree(inorderArr)