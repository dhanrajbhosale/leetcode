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
    public ListNode swapPairs(ListNode head) {
        if(head==null||head.next==null) return head;
        
        ListNode temp;
        ListNode prv=new ListNode();
        ListNode start=head.next;
        
        while(head!=null&&head.next!=null){
            temp=head;
            head=head.next;
            temp.next=head.next;
            head.next=temp;
            prv.next=head;
            head=temp.next;
            prv=temp;
        }
        
        return start;
    }
}