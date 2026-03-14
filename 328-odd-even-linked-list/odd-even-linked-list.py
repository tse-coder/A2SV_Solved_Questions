# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        odd = head
        todd = odd
        even = odd.next
        teven = even
        while todd and todd.next and teven.next:
            todd.next = todd.next.next
            teven.next = teven.next.next
            todd = todd.next
            teven = teven.next
        todd.next = even
        return odd