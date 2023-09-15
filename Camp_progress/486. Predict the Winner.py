class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
         return self.help(nums, 0, len(nums) - 1, len(nums)) >= 0

    def help(self, nums, i, j, n):
        if i == j:
            return nums[i]
        
        left = nums[i] - self.help(nums, i + 1, j, n)
        right = nums[j] - self.help(nums, i, j - 1, n)
        
        return max(left, right)
        
