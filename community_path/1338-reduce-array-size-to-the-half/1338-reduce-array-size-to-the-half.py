class Solution(object):
    def minSetSize(self, arr):
        counted = Counter(arr)
        ordered = sorted(counted, key = counted.get, reverse = True)
        count , store= 0,0
        n=ceil(len (arr) /2)
        i= 0
        
        while store < n:
            count +=1
            store += counted[ordered[i]]
            i +=1
        return count
    