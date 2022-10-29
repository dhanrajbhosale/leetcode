class Solution:
    def earliestFullBloom(self, p: List[int], g: List[int]) -> int:
        # take grouth sorted in descending
        # after first growth + plant, plant will run parallely so second growth+ plant+ prev growth only
        # return max of all of this
        
        # sort by growth
        t = sorted(zip(g, p), reverse=True)
        
        # first growth and plant
        res = [t[0][0]+t[0][1]]
        for i in range(1, len(t)):
            # add next Growths and Plants and prev Growths
            res.append(t[i][0]+t[i][1]+res[i-1]-t[i-1][0])
        return max(res)
        
    