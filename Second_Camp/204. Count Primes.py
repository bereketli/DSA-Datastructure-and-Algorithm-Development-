class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
           return 0

        primes = [True] * n
        for i in range(2, n):
            primes[i] = True

        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                for j in range(i * i, n, i):
                    primes[j] = False

        count = 0
        for i in range(2, n):
            if primes[i]:
                count += 1
        return count

            
