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
//solution 1
class Solution {
    
        public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        
        if(list1==null) return list2;
        if(list2==null) return list1;
        
     
           if(list1.val<list2.val){
               list1.next=mergeTwoLists(list1.next,list2);
                return list1;               
           }
           else{
               list2.next=mergeTwoLists(list1,list2.next);
               return list2;
           }        
    }
    
    public ListNode mergeKLists(ListNode[] lists) {
        if(lists.length==0) return null;
            ListNode temp=lists[0];
        for(int i=1;i<lists.length;i++)
            temp=mergeTwoLists(temp,lists[i]);      
           return temp;
}
    
    
    
    
}





// Solution 2
// class Solution {
//     public ListNode mergeKLists(ListNode[] lists) {
//    LinkedList<Integer> ll= new LinkedList<Integer>();
//         for(ListNode l : lists){
//             while(l!=null){
//                 ll.add(l.val);
//                 l=l.next;
//             }
//         }
//         Collections.sort(ll);
//         ListNode head=new ListNode();
//         ListNode h=head;
//         for(int i:ll){
//             ListNode t=new ListNode(i);
//             h.next=t;
//             h=t;
//         }
//         return head.next;
// }
// }

