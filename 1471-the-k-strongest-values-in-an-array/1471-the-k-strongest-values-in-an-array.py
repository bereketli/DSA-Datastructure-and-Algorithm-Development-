class Solution(object):
    def getStrongest(self, arr, k):
        arr.sort()
        output=[]
        l, r, mid_value =0, len(arr) - 1, arr[int((len(arr)-1) / 2)]
        while len(output) < k and l <= r:
            while len(output) <k and abs(mid_value - arr[r]) >= abs(mid_value - arr[l]):
                output.append(arr[r])
                r -=1
            if len(output) < k:
                output.append(arr[l])
            l +=1
        return output
            
                
        
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        