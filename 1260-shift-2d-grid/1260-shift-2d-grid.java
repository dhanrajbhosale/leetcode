class Solution {    
    public List<List<Integer>> shiftGrid(int[][] grid, int k) {
        int row=grid.length;
        int column=grid[0].length;
        int res[][]=new int[row][column];
        
        for(int i=0;i<row; i++){
            for(int j=0; j<column; j++){
                /*2D to 1 D to new 1D
                    i*column+j = current 1D position
                    i*column+j+K = new 1D position
                    (i*column+j+k)%(row*column) = handling out of bound to start from 0
                */
                int newVal=(i*column+j+k)%(row*column);
                int newR=newVal/column;
                int newC=newVal%column;
                res[newR][newC]=grid[i][j];
            }
        }
        return (List)Arrays.asList(res);
    }
}