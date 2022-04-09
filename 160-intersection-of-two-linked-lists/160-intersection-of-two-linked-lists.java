/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
//Solution 1
// public class Solution {
    
//     public int getLength(ListNode head){
//         ListNode temp=head;
//         int cnt=0;
//         if(temp==null) return 0;
        
//         while(temp!=null){
//             temp=temp.next;
//             cnt++;
//         }
//         return cnt;
        
//     }
    
    
//     public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        
//         int lA=getLength(headA);
//         int lB=getLength(headB);
//         int diff=Math.abs(lA-lB);
        
//         if(lA>lB){
//             for(int i=0;i<diff;i++)
//                 headA=headA.next;
            
//         }
//         else{
//             for(int i=0;i<diff;i++)
//                 headB=headB.next;
//         }
        
        
//         while(headA!=headB){
//             headA=headA.next;
//             headB=headB.next;
//         }
        
        
//         return headA;
//     }
// }

//Solution 2 (Withought Knowing diff of len
 public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        if(headA == null || headB == null) return null;

        ListNode a = headA;
        ListNode b = headB;
        //if a & b have different len, then we will stop the loop after second iteration
        while( a != b){
            //for the end of first iteration, we just reset the pointer to the head of another linkedlist
            a = a == null? headB : a.next;
            b = b == null? headA : b.next;    
        }

        return a;
    }
 }