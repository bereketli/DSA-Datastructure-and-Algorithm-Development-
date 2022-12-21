class Solution(object):
    def findClosestElements(self, arr, k, x):
        min_d, count =0, 1
        for i in range(1,len(arr)):
             minimum  =min(abs(arr[min_d] - x), abs(arr[i] - x))
             if minimum  != abs(arr[min_d] - x):
                  min_d = i
                             
        
        if min_d == 0:
                return arr[0:k]
        else:
            l = min_d - 1
        if min_d == len(arr)-1:
             return arr[-k:]
        else:
            r = min_d + 1
        while count < k:
            
            while count < k and l>=0 and abs(x - arr[l]) <= abs(x - arr[r]):
                count +=1
                l -=1
          
            while count <k and r <len(arr) and l>=0 and abs(x- arr[r]) < abs(x -  arr[l]):
                count +=1
                r +=1
                
            
            while count <k and r >= len(arr):
                
                count +=1
                l -=1
            
            while count < k and l < 0:
                count +=1
                r +=1
            
        return arr[l+1:r]
                
                
            