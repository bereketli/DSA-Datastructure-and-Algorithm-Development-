class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        output = []
        even_sum = sum([even for even in nums if even % 2 == 0 ])
        
        for  value in queries:
            current_sum = nums[value[1]] + value[0]
            
            if current_sum % 2 == 0:
                if nums[value[1]] % 2 == 0:
                    even_sum += value[0]
                else:
                    even_sum += current_sum
                output.append(even_sum)
                nums[value[1]]  = current_sum
            else:
                if nums[value[1]] % 2 == 0:
                    even_sum -= nums[value[1]]
                output.append(even_sum)    
                nums[value[1]]  = current_sum
            
        return output

