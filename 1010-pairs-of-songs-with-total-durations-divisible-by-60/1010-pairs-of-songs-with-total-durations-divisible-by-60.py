class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        dic = collections.defaultdict(int)
        cnt=0
        dic[60]=0
        for t in time:
            m = t%60 
            n = m if m else 60
            if 60-n in dic:
                cnt+=dic[60-n]
            dic[m] += 1
        return cnt