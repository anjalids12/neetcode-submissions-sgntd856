class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #Hash_map
        element_count = Counter(nums)
        max_val = 0
        max_key = 0
        for k,v in element_count.items():
            if v > max_val:
                max_val = v
                max_key = k
        if max_val > len(nums) // 2:
            return max_key
            
