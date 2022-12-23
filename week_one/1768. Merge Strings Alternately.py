class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1_len, word2_len, output =len(word1), len(word2), []
        for i in range(min(word1_len, word2_len)):
            output.append(word1[i])
            output.append(word2[i])
        if word1_len > word2_len:
            output.extend(word1[word2_len : ])
        elif word1_len < word2_len:
            output.extend(word2[word1_len : ])
        return "".join(output)
        
