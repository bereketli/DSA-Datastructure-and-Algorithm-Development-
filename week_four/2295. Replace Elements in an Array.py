class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        count = {}
        output = [0] * len(nums)
        for i in range(len(nums)):
            count[nums[i]] = i
        for op in operations:
            count[op[1]] = count.pop(op[0])
        for key in count:
            output[count[key]] = key
        return output
        

        