class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        dic = collections.defaultdict(int)
        for num in nums:
            dic[num]+=1
        _sum = 0
        for k, v in dic.items():
            _sum+= k if v==1 else 0
        return _sum