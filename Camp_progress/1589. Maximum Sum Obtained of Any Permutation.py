class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        modulo = (10**9) +7
        nums.sort(reverse=True)
        n = len(nums)
        req_order = [0] * n

        # used to know which indexes are requested repeatedly
        for req in requests:
            req_order[req[0]] += 1
            if req[1] < n - 1:
               req_order[req[1] + 1] -= 1

        count_request = []
        sum = 0
        for i in range(n):
            sum += req_order[i]
            req_order[i] = sum
            count_request.append([i, sum])
        count_request.sort(key=lambda x:-x[1])

        permutated = [0] * n 
        for i in range(n):
            permutated[count_request[i][0]] = nums[i] 
        
        sum = 0
        prefix = []
        for i in range(n):
            sum += permutated[i]
            prefix.append(sum)
        
        maximum_sum = 0
        for req in requests:
            initial = prefix[req[0] -1] if req[0] != 0 else 0
            final = prefix[req[1]]
            maximum_sum += ( final - initial)
        return maximum_sum % modulo
        

        



       
        
