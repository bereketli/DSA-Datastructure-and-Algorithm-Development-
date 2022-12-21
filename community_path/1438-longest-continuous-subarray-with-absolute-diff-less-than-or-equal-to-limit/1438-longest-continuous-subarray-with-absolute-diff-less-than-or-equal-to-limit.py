class Solution(object):
    def longestSubarray(self, nums, limit):
        inc_mono_que=[] 
        dec_mono_que=[]   
        max_len=l=r=0
        def increasing_que(num):
             while inc_mono_que and inc_mono_que[-1]>num:
                 inc_mono_que.pop()
             inc_mono_que.append(num)
        def decreasing_que(num):
             while dec_mono_que and dec_mono_que[-1]<num:
                   dec_mono_que.pop()
             dec_mono_que.append(num)
        while r<len(nums):
             increasing_que(nums[r])
             decreasing_que(nums[r])
           
             if l<r and inc_mono_que and dec_mono_que and abs(dec_mono_que[0]-inc_mono_que[0])>limit:
                 if nums[l]==dec_mono_que[0]:
                      dec_mono_que.pop(0)
                 if nums[l] ==inc_mono_que[0]:
                      inc_mono_que.pop(0)
                 l+=1
             max_len=max(max_len,r-l+1)
             r+=1
            
        return max_len

        