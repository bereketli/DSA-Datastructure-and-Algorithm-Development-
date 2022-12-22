class Solution:
    def isPalindrome(self, s: str) -> bool:
        n =len(s)
        s = s.lower()
        print(s)
        l , r =0 , n - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l +=1
            while l < r and not s[r].isalnum():
                r -=1
            if s[l] != s [r]:
                return False
            l +=1
            r -=1
        return True
        