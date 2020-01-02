class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        j=0
        while j<len(nums):
            i=0
            while i<len(nums):
                if i<=j:
                    i += 1
                elif nums[i]+nums[j]==target:
                    return str(j),str(i)
                    break
                else:
                    i += 1
            j += 1