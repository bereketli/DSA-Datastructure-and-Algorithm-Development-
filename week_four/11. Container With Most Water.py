class Solution(object):
    def maxArea(self, height):
        maxarea, l, r =0, 0, len(height) -1
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            maxarea = max(area , maxarea)
            if height[r] < height[l]:
                r -=1
            else:
                l +=1
        return maxarea
        
        
        """
        height = [1,8,6,2,5,4,8,3,7]
        l=1  r = 4
        maxarea = 49

        
        :type height: List[int]
        :rtype: int
        """
        
