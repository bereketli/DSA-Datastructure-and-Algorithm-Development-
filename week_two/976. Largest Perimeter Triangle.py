class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        maxArea = 0
        lengthNums = len(nums)
        nums.sort()
        for i in range(lengthNums - 1, 1,-1):
            if nums[i] < nums[i - 1] + nums[i -2]:
                maxArea = nums[i] + nums[i - 1] + nums[i - 2]
                break
        return maxArea
