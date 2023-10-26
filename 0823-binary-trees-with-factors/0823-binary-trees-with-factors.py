class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        print(arr)
        bt_dict = {i:1 for i in arr}

        for  i in range(1, len(arr)):
            parent = arr[i]
            
            for j in range(i-1,-1,-1):
                child1 = arr[j]
                child2 = parent/child1
                # found pair
                if child2 in bt_dict:
                    print(parent, child1, child1)
                    bt_dict[parent]+= bt_dict[child1]*bt_dict[child2]

        return sum(bt_dict.values())%1000000007