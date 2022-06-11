class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next: return False
        fp=head.next.next
        sp=head.next
        while sp!=fp and fp and fp.next:
            sp=sp.next
            fp=fp.next.next       
        return fp==sp