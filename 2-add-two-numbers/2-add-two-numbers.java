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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        if(l1==null) return l2;
        if(l2==null) return l1;
        
        int carry=0;
        int res=0;
        int add=0;
        ListNode head=new ListNode();
        ListNode h=head;
            
        while(l1!=null || l2!=null){
            add= ((l1!=null)? l1.val:0 )+((l2!=null)? l2.val:0 )+carry;
            carry=add/10;
            ListNode t=new ListNode(add%10);
            h.next=t;
            h=t;
            if(l1!=null) l1=l1.next;
            if(l2!=null) l2=l2.next;
        }
        if(carry==1) {
            ListNode t=new ListNode(1);
            h.next=t;
        }
        
        return head.next;
    }
}