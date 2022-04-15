class Solution {
    public void reverseString(char[] s) {
        char t=s[0];
        for(int i=0, j=s.length-1;i<j;i++,j--){
            s[i]=s[j];
            s[j]=t;
            t=s[i+1];
        }
    }
}