class Solution:
    def topKFrequent(self, words: List[str], n: int) -> List[str]:
        dic = collections.defaultdict(int)
        for word in words:
            dic[word]+=1
        # sort the dict in desc order based on frequency, f frequency equal then sort dict in asc order based on alphabet.
        dic = sorted(dic, key= lambda item: (-dic[item], item))
        return dic [:n]