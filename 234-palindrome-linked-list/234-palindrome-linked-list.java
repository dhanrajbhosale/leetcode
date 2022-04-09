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
    public boolean isPalindrome(ListNode head) {
        if(head==null||head.next==null) return true;
        
        Stack<Integer> st=new Stack();
        ListNode start=new ListNode(0);
        ListNode sp=start, fp=start;
        start.next=head;
        
        while(fp!=null && fp.next!=null){
            sp=sp.next;
            fp=fp.next.next;
            st.push(sp.val);
        }
        if(fp!=null) sp=sp.next;
    
        while(!st.isEmpty() && sp.val==st.peek()){
            sp=sp.next;
            st.pop();
        }      
        if(st.isEmpty()) return true;
        return false;
    }
}












































