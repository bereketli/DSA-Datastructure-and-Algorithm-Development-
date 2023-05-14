import math
class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        count_subarray = 0
        for i in range(len(nums)):
            gcd_subarray = nums[i]
            for num2 in nums[i:]:
                gcd_subarray = math.gcd(gcd_subarray, num2)
                if gcd_subarray == k:
                    count_subarray += 1
                elif gcd_subarray < k:
                    break
        return count_subarray
            
                    
