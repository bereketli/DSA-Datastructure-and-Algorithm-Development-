class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        output =[]
        for i in range(len(l)):
            sub_arr = sorted(nums[l[i] : r[i] +1])
            difference = sub_arr[1] - sub_arr[0]
            for j in range(1,len(sub_arr)-1): 
                if sub_arr[j +1] - sub_arr[j] != difference:
                    difference = "false"
                    output.append(False)
                    break
           
            if (difference != "false"):
                output.append(True)
           
        return output
                
        """
        :type nums: List[int]
        :type l: List[int]
        :type r: List[int]
        :rtype: List[bool]
        """
        