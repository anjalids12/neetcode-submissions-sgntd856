class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #Hash_map
        # count_map = dict()
        # for i in nums:
        #     count_map[i] = count_map.get(i, 0) + 1
        #     if count_map[i] > len(nums)//2:
        #         return i 

        #Sorting
        # nums.sort()
        # return nums[len(nums)//2]

        #Moore's Voting Algo
        count = 1
        maj_ele = nums[0]
        for  i in nums[1:]:
            if count == 0:
                maj_ele, count = i, 1
            elif maj_ele == i:
                count += 1
            else:
                count -= 1
        if nums.count(maj_ele) > len(nums)//2:
            return maj_ele
        else:
            return -1
            
            

