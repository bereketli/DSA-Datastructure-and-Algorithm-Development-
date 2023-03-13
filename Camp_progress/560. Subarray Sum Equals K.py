class Solution(object):
    def subarraySum(self, nums, k):
        # 5
        # {3, 2, -4, 4}
        # {0:1 ,3:1 ,5:1, -1:1,  }
        pre ={0:1}
        out =0
        summed =0
        for num in nums:
            summed += num
            if summed -k in pre:
                out += pre[summed - k]
            if summed in pre :
                pre[summed] +=1
            else:
                pre[summed] =1
        return out