# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Sol 1 Recursive
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head or not head.next:
#             return head
#         newHead = self.reverseList(head.next)
#         head.next.next = head
#         head.next = None
#         return newHead

# Sol 2 Iterative
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            curr=head
            head=head.next
            curr.next=prev
            prev=curr
        return prev
            
            
        