class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        out = []
        i = 0
        while i < len(nums):
            temp = 0
            j = 0
            while j <= i:
                temp = temp + nums[j]
                j += 1
            out.append(temp)
            i += 1
        return out