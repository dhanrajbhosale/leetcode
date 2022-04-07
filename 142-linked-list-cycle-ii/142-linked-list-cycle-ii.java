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
    public ListNode detectCycle(ListNode head) {
   if(head==null||head.next==null) return null;
        
         ListNode sp=head;       
         ListNode fp=head;     
        
        do{
          sp=sp.next;
            fp=fp.next.next;
        }while(sp!=fp && fp!=null && fp.next!=null);
        
    
        if(sp==fp){ //loop detected
            sp=head;
            while(sp!=fp){
                sp=sp.next;
                fp=fp.next;
            }
            return sp;
        }
        return null;

    }
}