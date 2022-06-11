# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB: return None
    
        l1=headA
        l2=headB    
        while l1!=l2:
            l1=l1.next if l1 else headB
            l2=l2.next if l2 else headA
        # once both reset, len remaining for both will SAME, so if not intersecting, both will meet at None
        return l1