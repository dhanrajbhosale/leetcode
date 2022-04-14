

/** Recustion (Top Down Approach)
 * Question   : Climbing Stairs
 * Complexity : Time: O(2^n) ; Space: O(n)
 */
// class Solution {
//     public int climbStairs(int n) {
//         if (n<=2) 
//             return n;
//         return climbStairs(n - 1) + climbStairs(n - 2);
//     }
// }


/** Recustion + Memorization (Top Down Approach)
 * Question   : Climbing Stairs
 * Complexity : Time: O(n) ; Space: O(n)
 */
// Sol 1
// class Solution {
//     public int climbStairs(int n) {
//         Map<Integer, Integer> memo = new HashMap<>();
//         memo.put(1, 1);
//         memo.put(2, 2);
//         return climbStairs(n, memo);
//     }

//     private int climbStairs(int n, Map<Integer, Integer> memo) {
//         if (memo.containsKey(n)) {
//             return memo.get(n);
//         }
//         memo.put(n, climbStairs(n - 1, memo) + climbStairs(n - 2, memo));
//         return memo.get(n);
//     }
// }

//Sol 2
// class Solution {
//     public int climbStairs(int n) {
//         int dp[]=new int[n+1];
//         Arrays.fill(dp,-1);
//         dp[0]=0;
//         dp[1]=1;
//         return climbStairs(n, dp);
//     }

//     private int climbStairs(int n, int [] dp) {
//         if(dp[n]!=-1) return dp[n];
//         if(n==2) return 2;
//         return dp[n]=climbStairs(n-1,dp)+climbStairs(n-2,dp);
//     }
// }


/** DP (Bottom Up Approach)
 * Question   : Climbing Stairs
 * Complexity : Time: O(n) ; Space: O(n)
 */
// class Solution {
//     public int climbStairs(int n) {
//         if (n <= 1) {
//             return 1;
//         }
        
//         int[] dp = new int[n + 1];
//         dp[1] = 1;
//         dp[2] = 2;

//         for (int i = 3; i <= n; i++) {
//             dp[i] = dp[i - 1] + dp[i - 2];
//         }

//         return dp[n];
//     }
// }


/** DP + Optimization (Bottom Up Approach)

To calculate the new value we only leverage the previous two values. So we don't need to use an array to store all the previous values.
 * Question   : Climbing Stairs
 * Complexity : Time: O(n) ; Space: O(1)
 */
class Solution {
    public int climbStairs(int n) {
        if (n <= 1) {
            return 1;
        }

        int prev1 = 1;
        int prev2 = 2;

        for (int i = 3; i <= n; i++) {
            int newValue = prev1 + prev2;
            prev1 = prev2;
            prev2 = newValue;
        }

        return prev2;
    }
}