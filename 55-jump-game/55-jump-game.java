//SOLUTION 1
class Solution {
    public boolean canJump(int[] nums) {
        if(nums.length==0 || nums.length==1) return true;
        int temp=nums[0];
        if(temp==0) return false;
        
        for(int i =1; i<nums.length-1;i++){
            temp--;
            if(temp<nums[i]) temp=nums[i];
            if(temp==0) return false;
        }
        return true;
    }
}

//SOLUTION 2

// class Solution {
//     static boolean myRecursion(int[] nArray, int k){
 
//           if (k == 0)      
//             return true;      
//           else{
//               int i=0;
//                 for(i=k-1;i>=0;i--){
//                     if(nArray[i]>=Math.abs(k-i))
//                         break;
//                 }
//                 if(i<0)
//                     return false;
//               return(myRecursion(nArray,i));
//           }      
                  
//     }  
    
//     public boolean canJump(int[] nums) {
//         return myRecursion(nums,nums.length-1);
        
//     }
// }
