# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        heada = headA
        headb = headB

        while heada != headb:
            heada = heada.next if heada else headB
            headb = headb.next if headb else headA
        return heada