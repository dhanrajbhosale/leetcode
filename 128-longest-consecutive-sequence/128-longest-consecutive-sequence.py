#Sol 1 TC: O(n) 
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums) #O(n) remove duplicates
        best = 0
        for x in nums: #O(1) 
            if x - 1 not in nums: #if x is start of streak
                y = x + 1 
                while y in nums: #test y = x+1, x+2, x+3, ... and stop at the first number y not in the streak
                    y += 1
                best = max(best, y - x)
        return best
    
# class Solution {
#     TC: O(nlgn)
#     public int longestConsecutive(int[] nums) {
#         if(nums.length==0) return 0;
#         Arrays.sort(nums);
#         int max=0, cnt=0;   
#         for(int i=0;i<nums.length-1;i++){
#             if(nums[i+1]-nums[i]==0) continue; 
#             if(nums[i+1]-nums[i]==1) cnt++;           
#             else cnt=0;
#             max=Math.max(max,cnt+1);
#         }
#         return (max==0)?1:max;       
#     }
# }

# Solution 2
# class Solution {
#     public int longestConsecutive(int[] nums) {
#         if(nums.length==0) return 0;
#        TreeSet<Integer> ts=new TreeSet<Integer>();  //stores unique & sorted directly
#         int max=0, cnt=0;      
#         for(int i:nums) ts.add(i);
#         List<Integer> list= new ArrayList<Integer>(ts);     
#         for(int i=0;i<list.size()-1;i++){
#             if(list.get(i+1)-list.get(i)==1)  cnt++;           
#             else cnt=0;
#             max=Math.max(max,cnt+1);
#         }
#         return (max==0)?1:max;       
#     }
# }
