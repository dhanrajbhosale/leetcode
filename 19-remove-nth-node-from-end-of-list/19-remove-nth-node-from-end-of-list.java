/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        
        ListNode start = new ListNode(0);
        ListNode sp=start, fp=start;
        start.next=head;
        
        for(int i=1; i<=n+1; i++)
        fp = fp.next;
    
        while(fp!=null){
            fp=fp.next;
            sp=sp.next;          
        }        
        sp.next=sp.next.next;
        return start.next;        
    }
}