class Solution {
    public boolean canCross(int[] stones) {
        //hashmap of stone position and posible length of jumps. If no length means cant reach there
        HashMap<Integer, HashSet<Integer>> map=new HashMap<Integer, HashSet<Integer>>();
        for(int i=0;i<stones.length;i++){
            map.put(stones[i], new HashSet<>());
        }
        //default value
        map.get(stones[0]).add(1);
        // take currStone
        for(int i=0;i<stones.length;i++){
            int currStone=stones[i];
            //get possible jumps from currStone
            HashSet<Integer> jumps=map.get(currStone);
            
            for(int jump:jumps){
                //calc next pos after jump
                int pos= currStone+jump;
                //if reached last stone, return true
                if(pos==stones[stones.length-1]) return true;
                //check if pos have stone or water
                if(map.containsKey(pos)){
                    //add possible jumps from currStone
                    //avoid 0 or -ve for jump -1
                    if(jump-1>0)
                    map.get(pos).add(jump-1);
                    
                    map.get(pos).add(jump);
                    map.get(pos).add(jump+1);
                }
                    
            }
        }
        //haven't reached end, return false
        return false;
    }
}