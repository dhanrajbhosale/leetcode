class Solution {
    
   
      public int findTheWinner(int n, int k) {
        int res = 0;
        for (int i = 1; i <= n; ++i)
            res = (res + k) % i;
        return res + 1;
    }
}

// solution 2nd

// class Solution {
//     public int findTheWinner(int n, int k) {
// 	    // Initialisation of the LinkedList
//         LinkedList<Integer> participants = new LinkedList<>();
//         for (int i = 1; i <= n; i++) {
// 		    participants.add(i);
// 		}
		
// 		int lastKilled = 0;
// 		// Run the game
//         for (int i = 0; i < n; i++) {
//             for (int j = 0; j < k-1; j++) {
// 			    participants.add(participants.poll());
// 			}
//             lastKilled = participants.poll();
//         }
//         // Return the last one killed
//         return lastKilled;
//     }
// }

