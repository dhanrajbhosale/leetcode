class Solution:
    def topKFrequent(self, words: List[str], n: int) -> List[str]:
        words.sort()
        dic = collections.defaultdict(int)
        for word in words:
            dic[word]+=1
        dic = [k for k, v in sorted(dic.items(), key= lambda item: item[1], reverse=True)]
        return dic [:n]