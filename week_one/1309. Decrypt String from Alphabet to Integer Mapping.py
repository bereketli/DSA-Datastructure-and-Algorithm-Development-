class Solution:
    def freqAlphabets(self, s: str) -> str:
        output =""
        end = len(s) - 1
        while end >= 0:
            if s[end] == "#":
                output = chr(96 + int(s[end - 2: end])) + output
                end -= 3
            else:
                output = chr(96 + int(s[end])) + output
                end -= 1
        return output
