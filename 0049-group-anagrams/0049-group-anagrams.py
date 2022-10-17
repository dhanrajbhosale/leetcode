class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = collections.defaultdict(list)
        res = []
        for i, v in enumerate(strs):
            dic["".join(sorted(v))].append(i)
        for i in dic:
            res.append([strs[i] for i in dic[i]])
        return res