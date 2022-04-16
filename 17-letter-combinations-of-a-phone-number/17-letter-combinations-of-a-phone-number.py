class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        res = []
        mapping={
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz",
        }
        def backTrack(i, curStr):
            if len(curStr)==len(digits):
                res.append(curStr)
                return
            for c in mapping[digits[i]]:
                backTrack(i+1,curStr+c)
        if digits:
            backTrack(0,"")
        
        return res
        
#// JAVA Solution backtracking solution        
# class Solution {
#     public void myReccursion(List<String> res, String digit, int index, String curr, String [] mapping){
#         if(curr.length()==digit.length()){
#             res.add(curr);
#             return;
#         }
#         String letters=mapping[digit.charAt(index)-'0'];
#         for(int i=0;i<letters.length();i++)
#              myReccursion(res, digit,index+1,curr+letters.charAt(i),mapping);
#     }
    
#     public List<String> letterCombinations(String digits) {
#         List<String> res=new ArrayList<String>();
#         if(digits==null || digits.equals("")) 
#             return res;
#         String [] mapping={
#             "0",
#             "1",
#             "abc",
#             "def",
#             "ghi",
#             "jkl",
#             "mno",
#             "pqrs",
#             "tuv",
#             "wxyz"
#         };

#         myReccursion(res, digits,0,"",mapping);
#         return res;
#     }
# }