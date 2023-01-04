class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        index = 0
        spaced_string =[]
        for i in range(len(s)):
            if index < len(spaces) and i == spaces[index]:
                spaced_string.append(" ")
                index += 1

            spaced_string.append(s[i])
        return "".join(spaced_string)