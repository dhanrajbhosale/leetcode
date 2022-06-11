# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #find mid
        sp=fp=head
        while fp and fp.next:
            sp=sp.next
            fp=fp.next.next
        #reverse next half
        prv=None
        while sp:
            nxt=sp.next
            sp.next=prv
            prv=sp
            sp=nxt
        #compare 1st &  2nd half
        sp=head
        while prv:
            if prv.val!=head.val:
                return False
            prv=prv.next
            head=head.next
        return True
        