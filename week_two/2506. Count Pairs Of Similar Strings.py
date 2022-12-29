class Solution:
    def similarPairs(self, words: List[str]) -> int:
        count = 0
        for index,word in enumerate(words):
            words[index] = set(word)
        for index1, word1 in enumerate(words):
            for index2 in range(index1 + 1, len(words)):
                if word1 == words[index2]:
                    count += 1
        return count
        