# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def helper(node):
            if node.next == None:
                return node
            _next = helper(node.next)
            if node.val >= _next.val:
                temp = node
                newNode = ListNode(node.val,_next)
                del temp 
                return newNode
            else:
                return _next
        return helper(head)
            