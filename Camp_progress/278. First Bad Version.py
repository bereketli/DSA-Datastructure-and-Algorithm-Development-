# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        min_bad = n
        max_good =0
        left, right = 1, n
        while left <= right:
            if min_bad == max_good + 1:
                return min_bad
            mid = (left + right) // 2
            if isBadVersion(mid):
                min_bad = min(min_bad, mid)
                right = mid 
            else:
                max_good = max(max_good, mid)
                left = mid


            
