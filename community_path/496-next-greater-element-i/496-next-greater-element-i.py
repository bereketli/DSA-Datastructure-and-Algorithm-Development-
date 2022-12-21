class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        top=-1
        stack=[]
        output=["a"]*len(nums1)
        for i in range(len(nums2)):
           
            stack.append(nums2[i])
            top+=1
            
            while stack and nums2[i]>stack[top-1]:
                  if(stack[top-1] in nums1):
                        output[nums1.index(stack[top-1])]=nums2[i]
                  stack[top-1]=nums2[i]
                  stack.pop()
                  top-=1
                  
                  
                  
            
        for j in range(len(nums1)):
            if(output[j]=="a"):
                output[j]=-1
            
        return output
