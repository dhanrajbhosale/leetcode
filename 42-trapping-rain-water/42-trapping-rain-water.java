class Solution {
    public static int rMax(int h, int[]height){
        int max=height[h];
        for(int i=h+1;i<height.length;i++){
            if(max<height[i])
            max=height[i];
        }
        return max;
    }
    
    public static int lMax(int h, int[]height){
        int max=height[h];
        for(int i=h-1;i>=0;i--){
            if(max<height[i])
            max=height[i];
        }
        return max;
    }
    
    public int trap(int[] height) {
        int max=0;
        int temp=0;
        for(int i=1;i<height.length-1;i++){
            temp=Math.min(rMax(i,height),lMax(i,height));
            max=max+(temp-height[i]);
        }
        return max;
    }
}