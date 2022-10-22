class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = collections.defaultdict(int)
        for num in arr:
            dic[num]+=1
        return len(dic.values()) == len(set(dic.values()))
        