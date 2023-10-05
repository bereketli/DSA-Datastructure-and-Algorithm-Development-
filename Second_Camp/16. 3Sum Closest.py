class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = float('inf')
        for i in range(len(nums) - 2):
            closest = self.twoSumClosest(nums, target - nums[i], i)
            sum_ = nums[i] + closest
            if abs(sum_ - target) < abs(ans - target):
                ans = sum_
        return ans

    def twoSumClosest(self, nums, k, st):
        si = st + 1
        ei = len(nums) - 1
        ans = float('inf')
        while si < ei:
            _sum = nums[si] + nums[ei]
            if abs(_sum - k) < abs(ans - k):
                ans = _sum
            if _sum == k:
                return _sum
            elif _sum < k:
                si += 1
            else:
                ei -= 1
        return ans

        
