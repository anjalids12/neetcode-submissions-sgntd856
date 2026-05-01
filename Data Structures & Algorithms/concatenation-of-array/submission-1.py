class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        current_length = len(nums)
        for j in range(1):
            i = 0
            while(i<current_length):
                nums.append(nums[i])
                i += 1
        return nums
        