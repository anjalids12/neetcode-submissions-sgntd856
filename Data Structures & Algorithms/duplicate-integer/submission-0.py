class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_length = len(nums)
        total_sum  = (nums_length*(nums_length+1))/2
        sum = 0
        for ele in nums:
            sum = sum + ele
        if sum != total_sum:
            return True
        else:
            return False

        