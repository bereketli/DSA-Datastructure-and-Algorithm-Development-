class Solution(object):
    def maxArea(self, height):
        max_area , l, r =0,0,len(height)-1
        while l < r:
            
           
          
            while l < r and height[r] <= height[l]:
                 max_area = max(max_area , (r - l)* height[r])
                 r -=1
            max_area = max(max_area , (r - l)* min(height[r],height[l]))
            l +=1
        
        return max_area
        
        """
        :type height: List[int]
        :rtype: int
        """
        