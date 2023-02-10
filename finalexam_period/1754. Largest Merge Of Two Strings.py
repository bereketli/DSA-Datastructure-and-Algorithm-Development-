class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        word1, word2 = list(word1), list(word2)
        merged = []
        point_word1 = 0
        point_word2 = 0
        while point_word1 < len(word1) and point_word2 < len(word2):
            if ord(word1[point_word1]) > ord(word2[point_word2]):
                merged.append(word1[point_word1])
                point_word1 += 1
            elif ord(word1[point_word1]) < ord(word2[point_word2]):
                merged.append(word2[point_word2])
                point_word2 += 1
            else:
                if word1[point_word1:] > word2[point_word2:]:
                   merged.append(word1[point_word1])
                   point_word1 += 1
                elif word1[point_word1:] < word2[point_word2:]:
                    merged.append(word2[point_word2])
                    point_word2 += 1
                else:
                    merged.append(word1[point_word1])
                    point_word1 += 1
                    
        merged.extend(word1[point_word1:]) 
        merged.extend(word2[point_word2:]) 
        
        return "".join(merged)   