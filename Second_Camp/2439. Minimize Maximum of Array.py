class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        result = nums[0]
        prfix = 0
        for i in range(len(nums)):
            prfix += nums[i]
            avg = ceil(prfix / (i + 1))
            result = max(result, avg)
        return result
