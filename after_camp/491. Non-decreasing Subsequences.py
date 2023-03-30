class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        repeat = set()
        self.output = []
        def nondec(idx, arr):
            new = arr + []
            for i in range(idx, len(nums)):
                if new and new[-1] <= nums[i]:
                    new.append(nums[i])
                elif not new:
                    new.append(nums[i])
                if len(new) >= 2 and str(new) not in repeat:
                    li = [] + new
                    self.output.append(li)
                    repeat.add(str(li))
                
                nondec(i + 1,new)
                new.pop()
            return
        nondec(0,[])
        return self.output