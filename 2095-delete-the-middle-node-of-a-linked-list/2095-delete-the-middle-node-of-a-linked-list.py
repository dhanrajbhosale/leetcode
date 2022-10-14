# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head.next
        sp, fp = head, head.next.next
        
        while fp and fp.next:
            sp=sp.next
            fp=fp.next.next
        sp.next = sp.next.next
        return head
    
    