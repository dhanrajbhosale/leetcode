# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        fp, sp = head, head
        prv = None
        
        while fp and fp.next:
            prv = sp
            sp=sp.next
            fp=fp.next.next
        prv.next = sp.next
            
        return head