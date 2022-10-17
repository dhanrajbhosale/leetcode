class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = collections.defaultdict(int)
        res = []
        # dict for storing frequencies
        for i in nums:
            dic[i] +=1
               # sorting dictionary keys using values in descending order and returning top K elements
        return [k for k, v in sorted(dic.items(), key=lambda item: item[1], reverse=True)][:k]