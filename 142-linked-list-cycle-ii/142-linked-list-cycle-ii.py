# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return None
        sp=head.next
        fp=head.next.next
        
        while sp!=fp and fp and fp.next:
            sp=sp.next
            fp=fp.next.next
        if not fp or not fp.next: return None
        fp=head
        pos=0
        while fp!=sp:
            sp=sp.next
            fp=fp.next
            pos+=1
        return sp
        