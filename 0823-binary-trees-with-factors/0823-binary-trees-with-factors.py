class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        bt_dict = {i:1 for i in arr}
        total_bts = 0
        for  i in range(1, len(arr)):
            parent = arr[i]     
            for j in range(i-1,-1,-1):
                child1 = arr[j]
                child2 = parent/child1
                # found pair
                if child2 in bt_dict:
                    bt_dict[parent]+= bt_dict[child1]*bt_dict[child2]
            total_bts+=bt_dict[parent]%1000000007
        return (total_bts+1)%1000000007