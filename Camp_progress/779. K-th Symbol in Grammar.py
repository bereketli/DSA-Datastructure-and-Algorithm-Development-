class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def grammar (n,k):
            if n == 1:
                return 0
            previous = grammar(n-1, (k + 1)//2) if k %2 ==1 else 1 - grammar(n-1, (k + 1)//2)
            return previous
        return grammar(n, k)
        
        
         
                    
                
