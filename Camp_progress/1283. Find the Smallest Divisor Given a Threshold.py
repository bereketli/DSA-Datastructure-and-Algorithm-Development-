class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l = 1
        r = max(nums)
        while l <= r:
            divisor = (l + r) // 2
            sum_division = 0
            for num in nums:
                sum_division += ceil((num) / divisor)
            if sum_division <= threshold:
                r = divisor - 1
            else:
                l = divisor + 1
        return l
        """
        l <- 1, r <- max(nums)
        if sum(mid results) <= thr, move r mid -1
        if sum(mid results) > thr, move l Mid + 1
        """