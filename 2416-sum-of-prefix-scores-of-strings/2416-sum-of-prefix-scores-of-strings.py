class Solution:

    def get_prefixes(self, s):
        l = len(s)
        res = []
        for i in range(1,l+1):
            res.append(s[:i])
        return res

    def sumPrefixScores(self, words: List[str]) -> List[int]:
        word_dic = collections.defaultdict(int)
        res = []
        for word in words: # cal freq of all possible prefixes
            for w in self.get_prefixes(word):
                word_dic[w]+=1
        
        for word in words: # cal prefix freq count for particular word
            cnt = 0
            for w in self.get_prefixes(word):
                cnt+=word_dic[w]
            res.append(cnt)
        return res