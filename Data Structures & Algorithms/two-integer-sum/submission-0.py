class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen=dict()
        for ind,ele in enumerate(nums):
            complement = target - ele
            if complement  not in seen:
                seen[ele] = ind
            else:
                return [seen[complement], ind]
        return [-1,-1]
