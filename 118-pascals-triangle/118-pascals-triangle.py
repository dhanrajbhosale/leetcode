#Solution 1 - logical
#Any row can be constructed using the offset sum of the previous row
 # 1 3 3 1 0 #4th row
 # +  0 1 3 3 1
 # =  1 4 6 4 1 #5th row
# def generate(self, numRows):
#         res = [[1]]
#         for i in range(1, numRows):
#             res += [map(lambda x, y: x+y, res[-1] + [0], [0] + res[-1])]
#         return res[:numRows]

#solution 2 
class Solution(object):    
    def generate(self, n):
        list1 = []
        for i in range (n):
            temp_list=[]
            #number of digit = row number
            for j in range (i+1):
                if j==0 or j==i:
                    #default 1st and last value
                    temp_list.append(1)
                else:
                    #sum from prev list
                    temp_list.append (list1[i-1] [j-1] + list1[i-1] [j])
            list1.append(temp_list)
        return list1


# #solution 3 - recursion
# class Solution(object):
#     def generate(self, numRows):
#         """
#         :type numRows: int
#         :rtype: List[List[int]]
#         """
#         if numRows==1:
#             return [[1]]
#         if numRows==2:
#             return [[1],[1,1]]
        
#         prev=self.generate(numRows-1)
#         temp=prev[-1]
#         res=[[1]]
#         for i,v in enumerate(temp):         
#             if i==(numRows-2):
#                 break
#             res[0].append(v+temp[i+1])
#         res[0].append(1)
#         return prev+res
            