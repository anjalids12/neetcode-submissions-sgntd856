class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # max_sum = float('-inf')
        # for i in range(len(nums)):
        #     sum_val = 0
        #     for j in range(i, len(nums)):
        #         sum_val += nums[j]
        #         if sum_val>max_sum:
        #             max_sum=sum_val
        # return max_sum

        max_sum = float('-inf')
        sum_val = 0
        for i in nums:
            sum_val += i
            if sum_val>max_sum:
                max_sum = sum_val
            if sum_val < 0: 
                sum_val = 0
        return max_sum
