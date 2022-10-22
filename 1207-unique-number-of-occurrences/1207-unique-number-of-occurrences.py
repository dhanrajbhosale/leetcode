class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = collections.defaultdict(int)
        dic_set = set()
        for num in arr:
            dic[num]+=1
        for num in dic.values():
            if num in dic_set:
                return False
            dic_set.add(num)
        return True
        