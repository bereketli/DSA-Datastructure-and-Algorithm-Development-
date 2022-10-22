class Solution(object):
    def longestMountain(self, arr):
        output, first =0, 0
        n = len(arr)
        while first < n:
            r = first
            if r + 1 < n and arr[r] < arr[r + 1]:
                while r + 1 < n and arr[r] < arr[r + 1]:
                    r +=1
                if  r +1 < n and arr[r] > arr[r + 1]:
                    
                      while r + 1 < n and arr[r] > arr[r + 1]:
                           r +=1
                      output = max(output, r - first + 1)
            first = max(r, first + 1)
        return output
                    
       
                
            
        """
        :type arr: List[int]
        :rtype: int
        """
        