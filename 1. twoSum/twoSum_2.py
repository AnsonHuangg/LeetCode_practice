class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i=0
        while i<len(nums):
            if target - nums[i] in nums[i+1:]:
                if target - nums[i] != nums[i]:
                    return [i,nums.index(target - nums[i])]
                    break
                else:
                    return [i,nums.index(target-nums[i],i+1,len(nums))]
                    break
            else:
                i += 1