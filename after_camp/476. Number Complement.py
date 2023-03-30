class Solution:
    def findComplement(self, num: int) -> int:
         bit_len = floor( math.log2( num ) ) + 1
         return num ^ ((2 ** bit_len) - 1)