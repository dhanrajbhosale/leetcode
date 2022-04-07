class Solution {
    public int longestConsecutive(int[] nums) {
        if(nums.length==0) return 0;
        Arrays.sort(nums);
        int max=0, cnt=0;   
        for(int i=0;i<nums.length-1;i++){
            if(nums[i+1]-nums[i]==0) continue; 
            if(nums[i+1]-nums[i]==1) cnt++;           
            else cnt=0;
            max=Math.max(max,cnt+1);
        }
        return (max==0)?1:max;       
    }
}

//Solution 2
// class Solution {
//     public int longestConsecutive(int[] nums) {
//         if(nums.length==0) return 0;
//        TreeSet<Integer> ts=new TreeSet<Integer>();  //stores unique & sorted directly
//         int max=0, cnt=0;      
//         for(int i:nums) ts.add(i);
//         List<Integer> list= new ArrayList<Integer>(ts);     
//         for(int i=0;i<list.size()-1;i++){
//             if(list.get(i+1)-list.get(i)==1)  cnt++;           
//             else cnt=0;
//             max=Math.max(max,cnt+1);
//         }
//         return (max==0)?1:max;       
//     }
// }