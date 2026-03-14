# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,head):
        prev = None
        curr = head
        while curr:
            _next = curr.next
            curr.next = prev
            prev = curr
            curr = _next
        return prev

    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = self.reverse(head)
        temp = head
        while temp and temp.next:
            if temp.next.val < temp.val:
                trash = temp.next
                temp.next = temp.next.next
                del trash
            else:
                temp = temp.next
        
        head = self.reverse(head)
        return head