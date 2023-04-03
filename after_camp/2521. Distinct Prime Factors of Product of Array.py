class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        sieve_primes, sieve_nums = [], [i for i in range(2, 1000)]
        count_primes = 0
        for num in sieve_nums:
            if num :
              sieve_primes.append(num)
              j = num ** 2
              while j < 1000:
                    
                    sieve_nums[j - 2] = 0
                    j += num
          
        for prime in sieve_primes:
          for num in nums:
            if num % prime == 0:
              count_primes += 1
              break
        
        return count_primes
            
        
