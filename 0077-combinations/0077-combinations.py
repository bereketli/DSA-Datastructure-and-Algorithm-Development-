class Solution(object):
    def combine(self, n, k):
        self.k = k
        self.sln = []
        self.size = n
        def combination(index, arr):
            i = index
            for i in range(index, (self.size - (self.k - 1)) + 1 + len(arr)):
                arr.append(i) 
                if len(arr) < self.k:
                   combination(i + 1, arr)
                elif len(arr) == self.k:
                    new = [] + arr
                    self.sln.append(new)
                 
                arr.pop()
                
            return
            
        
        
        combination(1,[])
       
        return self.sln
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        