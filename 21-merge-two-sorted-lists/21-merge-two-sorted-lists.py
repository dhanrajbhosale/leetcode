# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
        if not a:
            return b 
        if not b:
            return a
        
        if a.val>b.val:
            b.next=self.mergeTwoLists(a,b.next)
            return b
        else:
            a.next=self.mergeTwoLists(a.next,b)
            return a
    
    # iteratively
    # def mergeTwoLists1(self, l1, l2):
    #     dummy = cur = ListNode(0)
    #     while l1 and l2:
    #         if l1.val < l2.val:
    #             cur.next = l1
    #             l1 = l1.next
    #         else:
    #             cur.next = l2
    #             l2 = l2.next
    #         cur = cur.next
    #     cur.next = l1 or l2
    #     return dummy.next
        