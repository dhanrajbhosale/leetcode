class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res=[]
        # result n, totla closed, opened, curStr
        def myRecursion(res, n, c, o, curStr):
            if(n==c):
                res.append(curStr)
                return
            if o>c:
                myRecursion(res, n, c+1, o, curStr+")")
            if n>o:
                myRecursion(res, n, c, o+1, curStr+"(")
            
            
        myRecursion(res, n, 0, 0,"")
        
        return res
        