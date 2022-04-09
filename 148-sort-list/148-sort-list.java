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
    public ListNode sortList(ListNode head) {
        
        LinkedList<Integer> ll=new LinkedList<Integer>();
        
        while(head!=null){
            ll.add(head.val);
            head=head.next;
        }
        
        Collections.sort(ll);
        
        ListNode head1=new ListNode();
        ListNode h=head1;
        for(int i:ll){
            ListNode t=new ListNode (i);
            h.next=t;
            h=t;
        }
        return head1.next;
    }
}