/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        
        if(head==null||head.next==null) return false;
        
         ListNode sp=head;       
         ListNode fp=head;     
        
        do{
          sp=sp.next;
            fp=fp.next.next;
        }while(sp!=fp && fp!=null && fp.next!=null);
        return sp==fp;
    }
}