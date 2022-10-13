class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        _max, _sum = max(milestones), sum(milestones)
        if _sum -_max>= _max:
            return _sum
        return 2*(_sum -_max)+1
            

        