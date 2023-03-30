class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        diff = set()
        def permutation(arr):
          
            new_arr = [] + arr
            for num  in nums:
                if num in diff:
                    continue
                new_arr.append(num)
                diff.add(num)
                permutation(new_arr)
                if len(new_arr) == len(nums):
                    output.append([] + new_arr)
                popped = new_arr.pop()
                diff.remove(popped)
            return

        permutation([])
        return output
