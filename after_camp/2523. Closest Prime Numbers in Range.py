class Solution:
       
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def sieve_of_eratosthenes(n):
            is_prime = [True] * (n + 1)
            is_prime[0] = is_prime[1] = False
            for i in range(2, int(n ** 0.5) + 1):
                if is_prime[i]:
                    for j in range(i ** 2, n + 1, i):
                        is_prime[j] = False
            return [i for i in range(n + 1) if is_prime[i]]
        
        erato_prime = sieve_of_eratosthenes(right)
        
        difference = float("inf")
        ans = [-1,-1]
       
        for i in range(len(erato_prime) - 1):
            if erato_prime[i] >= left and erato_prime[i + 1] - erato_prime[i] < difference:
                difference = erato_prime[i + 1] - erato_prime[i]
                ans = [erato_prime[i], erato_prime[i + 1]]
                
            
                
        return ans
