class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        
        def target_sum(idx, current_sum):
            if (idx, current_sum) in memo:
                return memo[(idx, current_sum)]
            
            if idx == len(nums):
                if current_sum == target:
                    return 1
                else:
                    return 0
            
            positive_ways = target_sum(idx + 1, current_sum + nums[idx])
            negative_ways = target_sum(idx + 1, current_sum - nums[idx])
            
            memo[(idx, current_sum)] = positive_ways + negative_ways
            
            return memo[(idx, current_sum)]
        
        return target_sum(0, 0)
