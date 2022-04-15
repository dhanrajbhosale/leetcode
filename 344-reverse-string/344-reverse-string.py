class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        i, j  = 0, len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1


#   // Java Solution      
# class Solution {
#     public void reverseString(char[] s) {
#         char t=s[0];
#         for(int i=0, j=s.length-1;i<j;i++,j--){
#             s[i]=s[j];
#             s[j]=t;
#             t=s[i+1];
#         }
#     }
# }        