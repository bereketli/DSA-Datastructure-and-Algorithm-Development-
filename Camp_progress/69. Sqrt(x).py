class Solution:
    def mySqrt(self, x: int) -> int:
        left = 1
        right = x
        max_left = 0
        while left <= right:
            mid = (left + right) // 2
            if mid**2 > x:
                right = mid - 1
            elif mid**2 < x:
                left = mid +1
                max_left = mid
            else:
                return mid
        return int(max_left)




        
