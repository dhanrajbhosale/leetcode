class Solution {
    public static int maxSubArray(int[] A) {
        int maxvalue=A[0];
        int maxsofar=A[0];
        
        for(int i=1;i<A.length;i++){
            maxvalue=Math.max(maxvalue+A[i],A[i]);
            maxsofar=Math.max(maxsofar,maxvalue);
        }      
    return maxsofar;      
}
}
