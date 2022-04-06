class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] result={0,1};
        for(int i=0;i<nums.length;i++){
            for(int j=0;j<nums.length;j++){
                int sum=nums[i]+nums[j];
                if(sum==target && i!=j){
                    result[0]=i;
                    result[1]=j;
                    return result;
                }
            }
        }
        
        return result;
        
    }
}