class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = collections.defaultdict(list)
        for v in strs:
            dic["".join(sorted(v))].append(v)
        return dic.values()
    
    