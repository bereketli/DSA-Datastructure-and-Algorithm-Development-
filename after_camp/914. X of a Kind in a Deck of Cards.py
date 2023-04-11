class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        def primefact(n):
            divisor = 2
            new_prime = set()
            while divisor**2 <= n:
                while n % divisor == 0:
                    new_prime.add(divisor)
                    n //= divisor
                divisor += 1
            if n > 1:
                new_prime.add(n)
            return new_prime
        count = Counter(deck)
        prime= primefact(count[deck[0]])
        
     
        for ky in count:
            prime = prime.intersection(primefact(count[ky]))
            if  not prime:
                return False
        return True 
                




       
