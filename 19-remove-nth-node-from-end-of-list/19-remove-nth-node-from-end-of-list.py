# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fp=sp= head
        for _ in range(n):
            fp=fp.next
        if not fp: return head.next #The standard solution, but without a dummy extra node. Instead, simply handle the special case of removing the head right after the fast cursor got its head start
        while fp.next:
            fp=fp.next
            sp=sp.next
        sp.next=sp.next.next
        return head
    
             
            
        