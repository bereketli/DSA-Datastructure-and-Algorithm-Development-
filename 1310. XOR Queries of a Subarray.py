class Solution(object):
    def xorQueries(self, arr, queries):
        sum_xor=0
        xor_prefi=[]
        output =[]
        for i in range(len(arr)):
            sum_xor ^= arr[i]
            xor_prefi.append(sum_xor)
        for left, right in queries:
            if left==0:
                ans=xor_prefi[right]
            else:
                ans = xor_prefi[right] ^ xor_prefi[left-1]
        
         
            output.append(ans)
        
        
        return output
        """
        :type arr: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        