class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        minDiff = math.inf
        dic = collections.defaultdict(list)
        arr.sort()                                         #O(n log n) time

        for i in range(len(arr)-1):                        #O(n) time
            diff = arr[i+1] - arr[i]
            dic[diff].append([arr[i], arr[i+1]])           #O(n) space if all the pairs have the same minimum difference
            minDiff = min(minDiff, diff)
        return dic[minDiff]