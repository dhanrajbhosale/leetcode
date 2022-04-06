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
    public ListNode mergeKLists(ListNode[] lists) {
   LinkedList<Integer> ll= new LinkedList<Integer>();
        for(ListNode l : lists){
            while(l!=null){
                ll.add(l.val);
                l=l.next;
            }
        }
        Collections.sort(ll);
        ListNode head=new ListNode();
        ListNode h=head;
        for(int i:ll){
            ListNode t=new ListNode(i);
            h.next=t;
            h=t;
        }
        return head.next;
}
}
