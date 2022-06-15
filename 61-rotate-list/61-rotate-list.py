# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #return if node len <=1
        if not head or not head.next: return head
        #find len and end point to first
        l=head
        ln=1
        while l.next:
            ln+=1
            l=l.next
        l.next=head
        # disconnect from len-k
        for i in range(1,ln-k%ln):
            head=head.next
        res=head.next
        head.next=None
        return res
        
        
            
        