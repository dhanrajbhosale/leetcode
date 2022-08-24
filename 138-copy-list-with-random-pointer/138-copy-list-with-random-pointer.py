"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
# optimum approach Time O(n), Space O(1)
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        # step 1 make copy and add next to original
        curr = head
        while curr:
            front = curr.next
            copy = Node(curr.val)
            curr.next = copy
            copy.next = front
            curr = front
        # step 2 update random pntr of copy
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr=curr.next.next    
        # step 3 separate copy and original list
        curr = head
        copyHead = copy = head.next
        while curr:
            curr.next= copy.next
            curr = curr.next
            if curr:
                copy.next = curr.next
            else:
                copy.next = None
            copy = copy.next            
        return copyHead     

# with hashmap Time: O(n) Space: O(n)
# class Solution:
#     def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
#         oldToCopy = { None : None}
        
#         curr = head
#         # makig a hashmap
#         while curr:
#             copy = Node(curr.val)
#             oldToCopy[curr] = copy
#             curr = curr.next
        
#         # update next and random pooint and make a copy list
#         curr = head  
#         while curr:
#             copy = oldToCopy[curr]
#             copy.next = oldToCopy[curr.next]
#             copy.random = oldToCopy[curr.random]
#             curr = curr.next
        
#         return oldToCopy[head]
    