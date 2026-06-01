class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        sum_val = 0

        start = 0          # start index of best subarray
        end = 0            # end index of best subarray
        temp_start = 0     # candidate start index

        for i in range(len(nums)):
            sum_val += nums[i]

            if sum_val > max_sum:
                max_sum = sum_val
                start = temp_start
                end = i

            if sum_val < 0:
                sum_val = 0
                temp_start = i + 1
        print(nums[start:end+1])
        return max_sum


        # max_sum = float('-inf')
        # for i in range(len(nums)):
        #     sum_val = 0
        #     for j in range(i, len(nums)):
        #         sum_val += nums[j]
        #         if sum_val>max_sum:
        #             max_sum=sum_val
        # return max_sum