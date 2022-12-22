class Solution:
    def isPalindrome(self, x: int) -> bool:
        orign_x = x
        if x < 0:
            return False
        else:
            num =0
            test = True
            while test:
                num = num * 10 + x % 10
                x = x//10
                if x== 0:
                    test = False
        if int(num) == orign_x:
            return True
        else: 
            return False

