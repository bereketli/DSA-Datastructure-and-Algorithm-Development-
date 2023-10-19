class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo = {}

        def partition(i, reduced_sum):
            if i >= len(nums) or reduced_sum <= 0:
                return reduced_sum == 0
            
            state = (i, reduced_sum)
            
            if state not in memo:
                memo[state] = partition(i + 1, reduced_sum - nums[i]) or partition(i + 1, reduced_sum)

            return memo[state]
        
        return sum(nums) % 2 == 0 and partition(0, sum(nums) / 2)
