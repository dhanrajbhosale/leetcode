class Solution {
    public void myReccursion(List<String> res, String digit, int index, String curr, String [] mapping){
        if(curr.length()==digit.length()){
            res.add(curr);
            return;
        }
        String letters=mapping[digit.charAt(index)-'0'];
        for(int i=0;i<letters.length();i++)
             myReccursion(res, digit,index+1,curr+letters.charAt(i),mapping);
    }
    
    public List<String> letterCombinations(String digits) {
        List<String> res=new ArrayList<String>();
        if(digits==null || digits.equals("")) 
            return res;
        String [] mapping={
            "0",
            "1",
            "abc",
            "def",
            "ghi",
            "jkl",
            "mno",
            "pqrs",
            "tuv",
            "wxyz"
        };

        myReccursion(res, digits,0,"",mapping);
        return res;
    }
}