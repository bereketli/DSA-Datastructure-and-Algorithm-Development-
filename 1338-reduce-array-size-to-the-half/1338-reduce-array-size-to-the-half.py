class Solution(object):
    def minSetSize(self, arr):
        counted = Counter(arr)
        ordered = sorted(counted, key = counted.get)
        ordered.reverse()
        count , i, store= 0,0,0
        n=ceil(len (arr) /2)
        
        while store < n:
            count +=1
            store += counted[ordered[i]]
            i +=1
        return count
            
        """
        :type arr: List[int]
        :rtype: int
        """
        