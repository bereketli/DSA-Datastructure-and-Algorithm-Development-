class Solution(object):
    def merge(self, nums1, m, nums2,n):
        i=j=0
        tempo=nums1[i]
        inserted=0
        while i<m+inserted and j<n:
           
            if tempo<nums2[j]:
                i+=1
                tempo=nums1[i]
            elif tempo>=nums2[j]:
              
                nums1.insert(i,nums2[j])
                nums1.pop()
                inserted+=1
                if tempo==nums2[j]:
                   i+=2
                   if i<len(nums1)-1:
                       tempo=nums1[i]
                    
                   
                else:
                   
                    i+=1
                j+=1
            
        while j<n:
            nums1[i]=nums2[j]
            i+=1
            j+=1
        
            
                
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        