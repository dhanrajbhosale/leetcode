class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        dic = collections.defaultdict(int)
        cnt=0
        # iterate and cal mod, if (60-currMod) alredy seen, then can pair up. so update cnt with (60-currMod) freq. and also +1 freq of currMod
        for t in time:
            currMod = t%60 
            # special case to deal with currMod=0
            n = currMod if currMod else 60
            cnt+=dic[60-n]
            dic[currMod] += 1
        return cnt