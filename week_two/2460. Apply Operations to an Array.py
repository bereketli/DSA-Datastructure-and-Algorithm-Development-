class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        
        left = -1
        for right in range(len(nums)):
           
            if left == -1 and nums[right] == 0:
                left = right
               
            elif nums[right] != 0 and left != -1:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
        return nums
            



