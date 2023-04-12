class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        self.maximum = [0,0]
        def bitwise_or(idx,ored):
            for i in range(idx, len(nums)):
                tempo = ored
                ored |= nums[i]
                if ored > self.maximum [0]:
                    self.maximum = [ored, 1]
                elif ored == self.maximum [0]:
                    self.maximum[1] += 1
                bitwise_or(i + 1,ored  )
                ored = tempo

            return
        bitwise_or(0,0)
        return self.maximum[1]


        
