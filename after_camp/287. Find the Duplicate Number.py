class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if nums[i] -1 != i  and nums[nums[i] -1] != nums[i]:
                index = nums[i]
                
                nums[i], nums[index - 1] = nums[index - 1], nums[i]
            else:
                i += 1
        for i in range(len(nums)):
            if i + 1 != nums[i]:
                return nums[i]