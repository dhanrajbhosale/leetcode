class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # solution 1 Using Sorting TC: O(nlogn) SC: O(1)
        # return sorted(nums)[len(nums)//2]
        
        # solution 2 Using Disctionary TC: O(2n) SC: O(n)
        # countEle = Counter(nums) 
        # for key in countEle.keys():
        #     if countEle[key] > len(nums) // 2:
        #         return key
        
        # solution 3 Boyer Moore's Voting Algorith TC: O(n) SC: O(1)
        majorEle, count = nums[0], 0
    
        for num in nums:
            if num == majorEle:
                count += 1
            elif count == 0:
                majorEle, count = num, 1
            else:
                count -= 1

        return majorEle