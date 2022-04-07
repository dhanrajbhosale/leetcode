class Solution {
    static boolean myRecursion(int[] nArray, int k){
 
          if (k == 0)      
            return true;      
          else{
              int i=0;
                for(i=k-1;i>=0;i--){
                    if(nArray[i]>=Math.abs(k-i))
                        break;
                }
                if(i<0)
                    return false;
              return(myRecursion(nArray,i));
          }      
                  
    }  
    
    public boolean canJump(int[] nums) {
        return myRecursion(nums,nums.length-1);
        
    }
}