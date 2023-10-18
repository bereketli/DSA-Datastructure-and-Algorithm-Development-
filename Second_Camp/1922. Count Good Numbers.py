class Solution:
    def countGoodNumbers(self, n: int) -> int:
        modulo = (10**9) + 7
        def power(num,index):
            if index==0:
                  return 1 
            tempo = power(num, index//2)
            if index%2==0:
                return (tempo*tempo) % modulo
            else:
                return (((tempo* tempo ) % modulo)*num) % modulo
        five = power(5,n//2)
        four = power(4, n//2)
        product = five * four if n % 2 == 0 else five * four * 5
        return (product % modulo)


                    
        
        
       

                
