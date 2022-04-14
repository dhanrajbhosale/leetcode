// Sol 1 recursion
// class Solution {
//     public int fib(int n) {
//         if(n<=1) return n;
//         return fib(n-1)+fib(n-2);
//     }
// }

//Sol 2 recursion + memorization (DP)
class Solution {
    private int fib(int n, int []dp){
        if(dp[n]!=-1) return dp[n];
        return dp[n]=fib(n-1,dp)+fib(n-2,dp);
    }

    public int fib(int n) {
        if(n<=0) return 0;
        int dp[]=new int [n+1];
        Arrays.fill(dp,-1);
        dp[0]=0;
        dp[1]=1;
        return fib(n,dp);
    }
}