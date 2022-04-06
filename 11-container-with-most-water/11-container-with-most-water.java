public class Solution {
    public int maxArea(int[] height) {
       int maxarea=0,l=0,r=height.length-1;
        
        while(l<r){ 
            maxarea=Math.max(maxarea,Math.min(height[r],height[l])*(r-l));
            if(height[r]>height[l])
                l++;
            else r--;
        }
        return maxarea;
    }
}
