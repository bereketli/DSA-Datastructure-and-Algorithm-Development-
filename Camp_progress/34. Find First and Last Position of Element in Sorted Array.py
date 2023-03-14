class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        output = []
        self.l = 0
        self.r = len(nums) - 1

        def left_finder(l,r):
            while l <= r:
                    mid = (l + r) // 2
                    if nums[mid] < target:
                        l = mid + 1
                    else:
                        r = mid - 1
            return l
            
        def right_finder(l, r): 
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] > target:
                    r = mid -1
                else:
                    l = mid + 1
            return r


        while self.l <= self.r:
            mid = (self.l + self.r) // 2
            if nums[mid] < target:
                self.l = mid + 1
            elif nums[mid] > target:
                self.r = mid - 1
            else:
                self.l = left_finder(self.l, mid )
                self.r = right_finder(mid, self.r)
                output.extend( [self.l, self.r])
                break
        return output if output else [-1,-1]
                
        
            

        