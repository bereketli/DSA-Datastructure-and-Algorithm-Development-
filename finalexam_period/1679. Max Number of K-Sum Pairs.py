class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        operation=0
        left = 0
        right = len(nums) - 1
        while left < right:
         
            while left < right and nums[left] + nums[right] >= k:
                
                if nums[left] + nums[right] == k:
                    operation+=1
                    right-=1
                    break
                right -=1
            left +=1
        return operation