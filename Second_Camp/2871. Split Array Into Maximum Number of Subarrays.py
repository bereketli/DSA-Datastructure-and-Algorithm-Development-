class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        prefix_and =  nums[0]
        for num in nums:
            prefix_and &= num
        if prefix_and != 0:
            return 1

        prefix_and =  nums[0]
        count_subarray = 0
        
        for idx, num in enumerate(nums):
            prefix_and &= num
            if prefix_and == 0:
                count_subarray += 1
                if idx < len(nums) - 1:
                    prefix_and = nums[idx + 1]
        return count_subarray


        

    
        
