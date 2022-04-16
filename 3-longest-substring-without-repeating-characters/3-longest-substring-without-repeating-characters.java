class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashMap<Character, Integer> mpp=new HashMap<Character, Integer>();
        int max=0;
        int r=0;
        int l=0;
        while(r<s.length())
        {
            if(mpp.containsKey(s.charAt(r))){
                l=Math.max(mpp.get(s.charAt(r))+1,l);
            }
            mpp.put(s.charAt(r),r);
            max=Math.max(r-l+1,max);
            r++;
        }
        return max;
    }
}


//Python Solution
// class Solution(object):
//     def lengthOfLongestSubstring(self, s):
//         """
//         :type s: str
//         :rtype: int
//         """
//         charSet=set()
//         #window left pointer
//         l=0
//         res=0
//         #window right pointer
//         for r in range(len(s)):
//             # if duplicate, start removing from left side until no duplicate
//             while s[r] in charSet:
//                 charSet.remove(s[l])
//                 l+=1
//             charSet.add(s[r])
//             res=max(res,r-l+1)
//         return res
                