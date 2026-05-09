class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #Hash_map
        count_map = dict()
        for i in nums:
            count_map[i] = count_map.get(i, 0) + 1
            if count_map[i] > len(nums)//2:
                return i 

        
